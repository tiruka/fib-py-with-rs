use pyo3::exceptions::PyTypeError;
use pyo3::prelude::{pyfunction, PyResult};
use pyo3::types::{PyDict, PyList};

use crate::fib_calcs::fib_number::fibonacci_number;
use crate::fib_calcs::fib_numbers::fibonacci_numbers;

fn process_numbers(input_numbers: Vec<Vec<i32>>) -> Vec<Vec<u64>> {
    input_numbers
        .into_iter()
        .map(|x| fibonacci_numbers(x))
        .collect()
}

#[pyfunction]
pub fn run_config<'a>(config: &'a PyDict) -> PyResult<&'a PyDict> {
    match config.get_item("number").unwrap() {
        Some(data) => match data.downcast::<PyList>() {
            Ok(raw_data) => {
                let processed_results: Vec<i32> = raw_data.extract::<Vec<i32>>().unwrap();
                let fib_numbers: Vec<u64> = processed_results
                    .iter()
                    .map(|x| fibonacci_number(*x))
                    .collect();
                let _ = config.set_item("Number Result", fib_numbers);
            }
            Err(_) => Err(PyTypeError::new_err(
                "paramber number is not a list of intergers",
            ))
            .unwrap(),
        },
        None => println!("Parameter number is not in the config"),
    }
    Ok(config)
}
