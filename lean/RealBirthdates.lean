import BiologicalAvoidance
import Mathlib.Algebra.Order.Archimedean.Real.Basic

namespace BiologicalAvoidance

/- The real-birthdate version of Alexander's population axioms. Label
uniqueness makes E a labelled simple directed graph, rather than a multigraph. -/
structure IsRealPopulation {A V : Type*} (E : V → V → A → Prop)
    (birth : V → ℝ) : Prop where
  label_unique : ∀ u v a b, E u v a → E u v b → a = b
  roots_finite : ∃ F : Finset V, ∀ v, (¬ ∃ u a, E u v a) → v ∈ F
  children_finite : ∀ u, ∃ F : Finset V, ∀ v a, E u v a → v ∈ F
  birth_finite : ∀ t : ℝ, ∃ F : Finset V, ∀ v, birth v ≤ t → v ∈ F
  born_lt : ∀ u v a, E u v a → birth u < birth v
  parents : ∀ v, (∃ u a, E u v a) → ∀ a, ∃ u, E u v a
  vertices_infinite : Infinite V

theorem natural_birthdates_to_real {A V : Type*} {E : V → V → A → Prop}
    {birth : V → ℕ} (h : IsPopulation E birth) :
    IsRealPopulation E (fun v => (birth v : ℝ)) := by
  constructor
  · exact h.label_unique
  · exact h.roots_finite
  · exact h.children_finite
  · intro t
    obtain ⟨n, hn⟩ := exists_nat_gt t
    obtain ⟨F, hF⟩ := h.birth_finite n
    refine ⟨F, ?_⟩
    intro v hv
    exact hF v (Nat.cast_lt.mp (lt_of_le_of_lt hv hn))
  · intro u v a he
    exact Nat.cast_lt.mpr (h.born_lt u v a he)
  · exact h.parents
  · exact h.vertices_infinite

theorem finite_alphabet_real_avoidance {A : Type*} [Fintype A] (s : ℕ → A)
    (h : ¬ EventuallyPeriodic s) :
    ∃ (E : (ℕ × A) → (ℕ × A) → A → Prop) (birth : (ℕ × A) → ℝ),
      IsRealPopulation E birth ∧
      ¬ ∃ v : ℕ → ℕ × A, ∀ k, E (v k) (v (k+1)) (s k) := by
  obtain ⟨E, hp, ha⟩ := finite_alphabet_avoidance s h
  exact ⟨E, fun v => (v.1 : ℝ), natural_birthdates_to_real hp, ha⟩

end BiologicalAvoidance
