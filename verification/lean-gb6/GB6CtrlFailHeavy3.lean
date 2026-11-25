import GB6Core
/-! w-gb6 CONTROL (expected to FAIL), heavy kernel evaluation. -/
namespace GB6
theorem K16 : (grid16.filter (fun n => D4s.all (fun k => dot k n % 16 == 0))).length = 33 := by decide +kernel
end GB6
