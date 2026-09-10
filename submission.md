# Draft VibeMathed entry

This is a local draft for review. Supply a stable public result URL and chosen
contributor attribution after publication. These fields do not submit anything.

**Name:** Classification of biologically unavoidable sequences

**Short name:** Biological unavoidability and eventual periodicity

**Problem statement:** Characterize the infinite sequences over a finite
alphabet which occur in every infinite gendered population satisfying finite
roots, finite outdegree, strictly increasing real birthdates with finite
sublevel sets, and a parent of each label at every non-root. Are any sequences
which are not eventually periodic biologically unavoidable?

**Posed by:** Samuel A. Alexander, *Biologically unavoidable sequences*,
Electronic Journal of Combinatorics 20(1), P31 (2013), Section 6, page 12.

**Year posed:** 2013, using the published question as the cited source; an
arXiv version exists from 2012, but this draft does not assign an earlier
question date without checking that specific revision.

**What was shown:** Every non-eventually-periodic sequence has an explicit
avoiding population. For binary sequences, the graph has two roots and at
most two children per vertex, with two complementary incoming labels at
every non-root. A decreasing nonnegative path offset shows that any matching
infinite path would force eventual periodicity. An indicator projection and
finite-copy lift extend the construction to all finite alphabets, including
vertex-gendered witnesses. Combined with Alexander's positive theorem, this
classifies the unavoidable sequences exactly as the eventually periodic ones.
Corollaries characterize universality in the explicit binary family and show
finite-observation and computability obstructions. The other original ordinal
and universal-object questions are not all claimed solved.

**Result:** Proved classification; equivalently a negative answer to the
existence question about a non-eventually-periodic unavoidable sequence.

**Proposed status:** Candidate / review pending.

**Proposed verification:** Lean-checked, statement unaudited, with the
explicit coverage note below; final tier is for the reviewer to determine.

**Verification note:** The accompanying pinned Lean project checks the new
finite-alphabet negative construction, including real-birthdate population
axioms, under the endpoint `finite_alphabet_real_avoidance`. The release
contains compiler output, source hashes and an axiom audit. The positive
direction is Alexander's published theorem, reproduced with a finite-boundary
repair; it is not part of an end-to-end Lean equivalence. Thue–Morse
aperiodicity and the universality/computability corollaries are prose proofs.
Local project modules were freshly checked using existing compiled artifacts
for pinned dependencies. No independent human mathematical review, independent
statement audit or worldwide priority claim is made.

**Method:** Explicit construction and argument.

**Field:** Combinatorics; infinite labelled directed graphs and infinite words.

**Solve date:** 2026-09-10.

**Model:** OpenAI Codex (GPT-6 family; exact deployment identifier not recorded).

**AI contribution:** The model developed the central construction, proofs,
formalization and exposition. The human user selected the paper and directed
the research. No independent human mathematical review is recorded. The
site's final contribution category should preserve that description rather
than imply human proof verification.

**Source URL:** To be supplied after the result artifact is published.

**Source name:** Manuscript and pinned Lean project.

**Publication:** Public repository announcement / manuscript, once published.

**Collaborators / publisher attribution:** To be supplied by the user.

The live [methodology](https://vibemathed.com/methodology) and
[submission form](https://vibemathed.com/submit) were inspected on
2026-09-10. This package makes no prediction of acceptance or significance score.
