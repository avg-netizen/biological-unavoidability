# Formal negative direction

- Lean: `leanprover/lean4:v4.32.0-rc1`.
- mathlib: `360da6fa66c1273b76b6b2d8c5666fd5ac2e3b56`.
- All transitive package revisions are in `lake-manifest.json`.

`BiologicalAvoidance.lean` contains the binary graph, decreasing-offset proof,
finite common-period argument, aperiodic indicator projection, explicit
natural-birthdate population predicate, and finite-alphabet avoiding lift.

`RealBirthdates.lean` defines the real-birthdate predicate with finite weak
sublevels at every real bound. It proves the natural-to-real conversion and
the endpoint `finite_alphabet_real_avoidance`.

`Audit.lean` prints that endpoint and the axioms of seven principal theorems.
The verifier expects only `propext`, `Classical.choice` and `Quot.sound`.
There are no project-local declared axioms or proof placeholders.

The positive direction is a cited and reproduced prose theorem, not a hidden
Lean axiom. No full equivalence is claimed as a formal endpoint. See the
[statement audit](../STATEMENT-AUDIT.md) before interpreting the result.
