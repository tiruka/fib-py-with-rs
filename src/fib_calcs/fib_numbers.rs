use crate::fib_calcs::fib_number::fibonacci_number;
use pyo3::prelude::pyfunction;
#[pyfunction]
pub fn fibonacci_numbers(numbers: Vec<i32>) -> Vec<u64> {
    numbers.iter().map(|&n| fibonacci_number(n)).collect()
}
