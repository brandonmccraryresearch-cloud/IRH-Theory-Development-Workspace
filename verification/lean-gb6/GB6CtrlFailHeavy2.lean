import GB6Core
/-! w-gb6 CONTROL (expected to FAIL), heavy kernel evaluation. -/
namespace GB6
theorem K03_Q : cntQ A4r = 1861 := by decide +kernel
end GB6
