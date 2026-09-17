# Provenance and contribution disclosure

Prepared 2026-09-10 as a self-contained submission package. It snapshots
earlier research notes on the classification and formal negative construction,
the prefix repair, and the universality and observation consequences; it does
not depend on those notes.

A human collaborator selected Alexander's paper and directed the research.
OpenAI Codex (GPT-6 family) developed the new construction, proofs, formalization,
checks and exposition. No more specific deployment identifier was recorded.

`BiologicalAvoidance.lean` is the original checked research source with an updated
header and its print commands moved into `Audit.lean`. `RealBirthdates.lean`
adds the real-birthdate bridge in this packaging pass. The negative theorem's
population hypotheses are proved, not introduced as external axioms.

The dependency manifest comes from the previously used Lean environment,
with the project name changed and the mathlib input revision pinned to its
full commit. The portable verifier accepts any matching dependency checkout;
the local run explicitly records reuse of existing compiled dependency caches.

No private correspondence, original chat transcript, access tokens or user
identity information is included.
