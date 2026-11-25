import GB6Core
/-! w-gb6 EXP-1304 C16 (combinatorial part): on the 16^4 grid x = 2πn/16 with the scaled
shell k ∈ D4s, the points where k·n ≡ 0 (mod 16) for all 24 k (i.e. every cos(k·x) = 1) number 32. -/
namespace GB6
theorem C16_grid_count :
    (grid16.filter (fun n => D4s.all (fun k => dot k n % 16 == 0))).length = 32 := by decide +kernel
theorem C16_grid_size : grid16.length = 65536 := by decide +kernel
end GB6
#print axioms GB6.C16_grid_count
#print axioms GB6.C16_grid_size
