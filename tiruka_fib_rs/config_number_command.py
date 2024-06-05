import argparse
import yaml
import os
from pprint import pprint
from .tiruka_fib_rs import run_config


def config_number_command() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate Fibonacci numbers with a config file"
    )
    parser.add_argument(
        "--config-path",
        action="store",
        dest="config_path",
        type=str,
        required=True,
        help="Config file path to use",
    )
    args = parser.parse_args()
    with open(str(os.getcwd()) + "/" + args.config_path, "r") as file:
        config_data = yaml.safe_load(file)
    pprint(config_data)
    pprint(run_config(config_data))
