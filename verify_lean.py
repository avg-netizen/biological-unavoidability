"""Compile every local module and audit endpoints against pinned dependencies.

Default: use lean/.lake/packages after normal Lake dependency setup.
Optional --packages-dir permits an existing dependency cache. Its revisions
and tracked working-tree state are checked and recorded. No dependency is
modified. A cached-dependency run is not described as a fresh dependency build.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import time

root = Path(__file__).resolve().parent
project = root / 'lean'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--packages-dir', type=Path)
args = parser.parse_args()
packages = (args.packages_dir or project / '.lake/packages').resolve()
manifest = json.loads((project / 'lake-manifest.json').read_text())
version = (project / 'lean-toolchain').read_text().strip()
binary = Path.home() / '.elan/toolchains' / version.replace('/', '--').replace(':', '---') / 'bin/lean'
report = {'toolchain': version, 'dependency_mode': 'existing cache' if args.packages_dir else 'project packages',
          'dependencies': [], 'sources': {}, 'steps': [], 'status': 'FAIL'}
logs = []
output = project / '.lake/build/lib/lean'
output.mkdir(parents=True, exist_ok=True)
env = os.environ.copy()
env['LEAN_PATH'] = os.pathsep.join([str(output)] + [str(packages / p['name'] / '.lake/build/lib/lean') for p in manifest['packages']])
error = None
try:
    for p in manifest['packages']:
        directory = packages / p['name']
        rev = subprocess.check_output(['git', '-C', str(directory), 'rev-parse', 'HEAD'], text=True).strip()
        # A copied dependency cache may have executable-bit changes. Ignore only file modes;
        # reject any tracked source-content change without altering the checkout.
        dirty = subprocess.run(['git', '-c', 'core.filemode=false', '-C', str(directory), 'diff', '--quiet', 'HEAD'], check=False).returncode
        report['dependencies'].append({'name': p['name'], 'expected': p['rev'], 'actual': rev, 'tracked_content_changes': dirty != 0})
        if rev != p['rev'] or dirty:
            raise RuntimeError(f"Dependency {p['name']} does not match the clean pinned revision")
    for name in ['BiologicalAvoidance.lean', 'RealBirthdates.lean', 'Audit.lean']:
        source = project / name
        text = source.read_text()
        if re.search(r'\b(sorry|admit|native_decide)\b|^\s*axiom\s', text, re.M):
            raise RuntimeError(f'Unexpected proof escape in {name}')
        report['sources'][name] = hashlib.sha256(source.read_bytes()).hexdigest()
        command = [str(binary)]
        if name != 'Audit.lean':
            command += ['-o', str(output / source.with_suffix('.olean').name)]
        command += [name]
        start = time.monotonic()
        result = subprocess.run(command, cwd=project, env=env, text=True, capture_output=True, timeout=600)
        combined = result.stdout + result.stderr
        logs.append(f'=== {name} ===\n{combined}')
        report['steps'].append({'source': name, 'exit_code': result.returncode, 'seconds': round(time.monotonic() - start, 3)})
        print(name, 'exit', result.returncode, flush=True)
        if result.returncode or 'sorryAx' in combined:
            raise RuntimeError(f'Lean check failed for {name}')
    audit = logs[-1]
    expected = {'path_forces_eventual_periodicity', 'binary_population', 'aperiodic_indicator',
                'lift_population', 'finite_alphabet_avoidance', 'natural_birthdates_to_real',
                'finite_alphabet_real_avoidance'}
    audited = set()
    for endpoint, axioms in re.findall(r"'BiologicalAvoidance\.([^']+)' depends on axioms: \[([^\]]*)\]", audit):
        used = {a.strip() for a in axioms.split(',') if a.strip()}
        if not used <= {'propext', 'Classical.choice', 'Quot.sound'}:
            raise RuntimeError(f'Unexpected axioms for {endpoint}: {used}')
        audited.add(endpoint)
    if not expected <= audited:
        raise RuntimeError(f'Missing audit output: {expected - audited}')
    report['audited_endpoints'] = sorted(audited)
    report['status'] = 'PASS'
except Exception as exc:
    error = str(exc)
    report['error'] = error
finally:
    (root / 'verification').mkdir(exist_ok=True)
    (root / 'verification/lean.log').write_text('\n'.join(logs))
    (root / 'verification/lean.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
raise SystemExit(0 if report['status'] == 'PASS' else 1)
