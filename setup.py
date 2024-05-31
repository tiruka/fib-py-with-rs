#!/usr/bin/env python
from setuptools import dist

dist.Distribution().fetch_build_eggs(["setuptools_rust"])
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="tiruka-fib-rs",
    version="0.1",
    rust_extensions=[
        RustExtension(
            ".fib-py-with-rs.tiruka_fib_rs", path="Cargo.toml", binding=Binding.PyO3
        )
    ],
    packages=["fib-py-with-rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Oprating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    zip_safe=False,
)
