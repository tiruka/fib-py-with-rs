#!/usr/bin/env python
from setuptools import dist

dist.Distribution().fetch_build_eggs(["setuptools_rust"])
from setuptools import setup  # noqa: E402
from setuptools_rust import RustExtension, Binding  # type: ignore # noqa: E402


setup(
    name="tiruka-fib-rs",
    version="0.1",
    rust_extensions=[
        RustExtension(
            ".tiruka_fib_rs.tiruka_fib_rs", path="Cargo.toml", binding=Binding.PyO3
        )
    ],
    packages=["tiruka_fib_rs"],
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
    entry_points={
        "console_scripts": [
            "fib-number = tiruka_fib_rs." "fib_number_command:" "fib_number_command",
        ]
    },
)
