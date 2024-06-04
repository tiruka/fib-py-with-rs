use crate::fib_calcs::fib_number::fibonacci_number;
use pyo3::prelude::pyfunction;
#[pyfunction]
pub fn fibonacci_numbers(numbers: Vec<i32>) -> Vec<u64> {
    numbers.iter().map(|&n| fibonacci_number(n)).collect()
}

#[cfg(test)]
mod fibonacci_numbers_tests {
    use super::fibonacci_numbers;

    #[test]
    fn test_run() {
        assert_eq!(fibonacci_numbers(vec![1, 2, 3, 20]), vec![1, 1, 2, 6765]);
    }
}
