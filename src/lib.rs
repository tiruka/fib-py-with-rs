use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
mod fib_calcs;
mod interface;

use fib_calcs::fib_number::fibonacci_number;
use fib_calcs::fib_numbers::fibonacci_numbers;
use interface::config::run_config;
use pyo3::{
    prelude::{pymodule, PyModule},
    PyResult,
};
#[pyfunction]
fn say_hello() {
    println!("saying hello from Rust!");
}

#[pymodule]
fn tiruka_fib_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(say_hello));
    m.add_wrapped(wrap_pyfunction!(fibonacci_number));
    m.add_wrapped(wrap_pyfunction!(fibonacci_numbers));
    m.add_wrapped(wrap_pyfunction!(run_config));
    Ok(())
}
