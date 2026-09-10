# Statement correspondence and coverage

This is a local audit by the same AI system that developed the proof. It is
not independent statement anchoring or expert review. The reference is
Alexander's published Definition 1 and Section 6, with zero-based sequence
indices replacing the paper's one-based convention.

## The negative endpoint

`finite_alphabet_real_avoidance` states: for every finite alphabet A and every
sequence s over A that is not eventually periodic, there exist an edge-label
predicate E on N x A and real birthdates such that E satisfies
`IsRealPopulation` and no infinite s-matching vertex sequence exists.

| Original condition | Formal representation | Assessment |
|---|---|---|
| A directed graph and a label function on its edges | Predicate `E u v a`, with `label_unique` | At most one label on each ordered pair. Taking an edge to mean existence of its label recovers a labelled simple directed graph. |
| Finitely many roots | `roots_finite` supplies a finite set containing all vertices with no incoming labelled edge | Equivalent finiteness condition; roots need not have been named in advance. |
| Each vertex has finitely many children | `children_finite` supplies a finite set containing every labelled successor | No global degree bound is assumed. The constructed witnesses have one. |
| Finite birthdate sublevels at every real bound | `birth_finite : ∀ t : ℝ, ... birth v ≤ t ...` | Uses the paper's weak inequality and real quantifier. |
| Birthdates strictly increase on edges | `born_lt` | Excludes loops, cycles and repeated vertices on any path. |
| Infinitely many vertices | `vertices_infinite : Infinite V` | Proved for N x A; the sequence itself supplies an element of A. |
| Every label occurs on an incoming edge at each non-root | `parents`, conditional on existence of any parent | Exactly the non-root condition, rather than a condition only on selected vertices. |
| A matching path can start anywhere | Negates existence of any `v : ℕ → ℕ × A` with the matching edges | No root or fixed-start restriction is introduced. |
| Finite alphabet {1,...,n}, n>0 | Arbitrary `Fintype A` and a sequence into A | Contains the paper's alphabets; finite relabelling changes no graph property. Empty A has no such sequence. |
| Target not eventually periodic | Negation of existence of a threshold and positive period | Positive period is explicit. Both eventual-period and eventual-antiperiod cases in the binary proof produce it. |

The existential witness type N x A is sufficient: disproving unavoidability
requires one admissible graph per target, not a representation of every possible
population on that type. Likewise natural-valued witness dates do not restrict
the original problem: the final theorem supplies their real embedding and
verifies the original real sublevel condition.

Unique edge labels supply the mathematical correspondence with the paper's
edge-label function. An explicit packaged graph structure with that function
is not a separate formal object here. This representational correspondence
should still be checked by an independent reader.

The aperiodic indicator in the finite-alphabet proof is obtained existentially.
The theorem does not assert an algorithm that identifies a suitable indicator
from an arbitrary sequence program. The computability reductions use the
explicit binary family, so they require no such selection procedure.

## Coverage table

| Manuscript assertion | Evidence |
|---|---|
| Binary matching path forces eventual periodicity | Lean `path_forces_eventual_periodicity` |
| Binary graph satisfies natural-birthdate population axioms | Lean `binary_population` |
| Aperiodic finite-alphabet sequence has an aperiodic binary indicator | Lean `aperiodic_indicator` |
| Finite-alphabet lifted witness and avoidance | Lean `lift_population`, `finite_alphabet_avoidance` |
| Real-birthdate witness and avoidance | Lean `natural_birthdates_to_real`, `finite_alphabet_real_avoidance`; check release log for successful execution |
| Exact two-root/two-child bounds and vertex-gendered description | Explicit prose checks; the full sharp cardinality assertions are not separate Lean endpoints |
| Eventual periodicity implies unavoidability | Alexander's theorem, with complete prose proof and boundary repair in Section 4 |
| Thue–Morse is aperiodic | Prose binary-digit argument |
| Universality of P_s iff s is eventually periodic | Prose proof using the negative theorem and a finite delayed quotient |
| Finite-observation obstruction and computability reductions | Prose corollaries with explicit constructions |

No missing positive-direction argument is assumed as a formal axiom. The final
equivalence is obtained mathematically by combining the checked negative
construction with the reproduced positive theorem. The finite controls do
not replace any infinite proof.
