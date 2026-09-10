"""Render the manuscript with Pandoc and Tectonic (no Python dependencies)."""
import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--allow-downloads', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parent
subprocess.run(['pandoc', 'paper.md', '-s', '--mathml', '--metadata', 'lang=en', '-o', 'paper.html'], cwd=root, check=True)
subprocess.run(['pandoc', 'paper.md', '-s', '-o', 'paper.tex'], cwd=root, check=True)
command = ['tectonic', '--keep-logs']
if not args.allow_downloads:
    command.append('--only-cached')
subprocess.run(command + ['paper.tex'], cwd=root, check=True)
