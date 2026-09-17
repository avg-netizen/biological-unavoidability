# Verification record

`lean.json` records the checker result, dependency revisions, source hashes,
module compilation outcomes and printed endpoints. `lean.log` contains the
compiler and audit output. Read the status field: a failed run never counts
as a successful proof check.

Local project modules are freshly compiled by `verify_lean.py`. The recorded
run uses existing compiled artifacts for pinned dependencies, with their
tracked source contents checked against the pinned revisions. Executable-bit
changes in the copied cache are ignored; no dependency is edited. This does
not claim that every dependency artifact was rebuilt from its source in this
run. The usual toolchain, kernel and compiled-dependency trust assumptions
remain.

The Python finite-control reports live in `../checks/*.json`. They are separate
from the Lean proof. `../SHA256SUMS` binds the release files. No external
statement audit is recorded.
