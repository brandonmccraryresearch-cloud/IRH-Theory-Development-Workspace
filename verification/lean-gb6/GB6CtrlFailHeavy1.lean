import GB6Core
/-! w-gb6 CONTROL (expected to FAIL), heavy kernel evaluation. -/
namespace GB6
theorem K01_Q : cntQ D4 = 3385 := by decide +kernel
end GB6
