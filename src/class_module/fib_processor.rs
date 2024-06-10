use crate::fib_calcs::fib_number::fibonacci_number;
use crate::fib_calcs::fib_numbers::fibonacci_numbers;

use pyo3::prelude::{pyclass, pymethods};

#[pyclass]
pub struct FibProcessor {
    #[pyo3(get, set)]
    pub number: Vec<i32>,

    #[pyo3(get, set)]
    pub numbers: Vec<Vec<i32>>,

    #[pyo3(get)]
    pub number_results: Vec<u64>,

    #[pyo3(get)]
    pub numbers_results: Vec<Vec<u64>>,
}

#[pymethods]
impl FibProcessor {
    #[staticmethod]
    pub fn process_numbers(input_numbers: Vec<Vec<i32>>) -> Vec<Vec<u64>> {
        input_numbers
            .into_iter()
            .map(|x| fibonacci_numbers(x))
            .collect()
    }

    #[new]
    fn new(number: Vec<i32>, numbers: Vec<Vec<i32>>) -> Self {
        let input_number = number.clone();
        let input_numbers: Vec<Vec<i32>> = numbers.clone();
        let number_results = input_number.iter().map(|&x| fibonacci_number(x)).collect();
        let numbers_results = input_numbers
            .into_iter()
            .map(|x| fibonacci_numbers(x))
            .collect();
        FibProcessor {
            number,
            numbers,
            number_results,
            numbers_results,
        }
    }
}
