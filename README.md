# Classification of biologically unavoidable sequences

Submission package, 10 September 2026. Read **[paper.pdf](paper.pdf)**,
or the equivalent [HTML](paper.html), [Markdown](paper.md) or [LaTeX](paper.tex).

The main theorem characterizes the biologically unavoidable finite-alphabet
sequences as exactly the eventually periodic ones. The new negative direction
constructs an avoiding population for every other sequence. Alexander's
positive direction is recalled with a finite-boundary proof repair.

## Contents

- `paper.*`: the self-contained manuscript and rendered formats.
- [lean/](lean/README.md): pinned Lean/mathlib project and endpoint audit.
- [STATEMENT-AUDIT.md](STATEMENT-AUDIT.md): comparison with the paper's axioms,
  formal coverage and unformalized claims.
- [verification/](verification/README.md): fresh local module checks, source
  hashes, dependency revisions and finite-control results.
- [checks/](checks/README.md): two independent standard-library Python controls.
- [literature-review.md](literature-review.md): sources, searches and limits.
- [PROVENANCE.md](PROVENANCE.md): AI contribution and artifact provenance.
- [submission.json](submission.json): VibeMathed entry fields.

## Reproduce

Install the Lean toolchain named in `lean/lean-toolchain`. From `lean/`:

```sh
lake update
lake exe cache get
```

The committed manifest pins every dependency; `lakefile.toml` also pins mathlib
by its full commit. From this directory run:

```sh
python3 verify_lean.py
python3 checks/classification.py
python3 checks/observation.py
```

The verifier compiles all local modules afresh and checks the printed endpoint
axioms. It refuses dependency revisions or tracked source contents that differ
from the pins. Executable-bit differences alone are ignored. Alternatively,
an existing matching dependency cache can be supplied with `--packages-dir`;
the verification report states that mode explicitly. No dependency is modified
by the Python verifier.

The recorded local run used existing pinned dependency artifacts. It is not
a fresh download or a source rebuild of all of mathlib. The project source,
manifest and commands have no dependency on the original research directory
layout. A conventional `lake build` and `lake env lean Audit.lean` are also
available after dependency setup; the recorded Python check is the precise
verification claim for this release.

Rebuild the documents with `python3 build_documents.py` after installing
Pandoc and Tectonic. The default uses cached TeX resources; pass
`--allow-downloads` to let Tectonic acquire missing resources.

## Status

The new negative construction has a formal endpoint; the complete
classification and the secondary results retain the coverage limits in
`STATEMENT-AUDIT.md`. There is no established literature priority. Candidate/review pending is the proposed
initial catalog status.
