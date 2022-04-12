"""Module to generate the output data frame."""

from typing import Tuple
import numpy as np
import pandas as pd


def process_input(input_filename: str = "./data/input-cleaned.csv", output_filename: str = "./data/output.csv") -> pd.DataFrame:
    """Group the data frame by weekday and return the mean sales quantity. Round the
    sales quantity and convert it to an integer.

    Args:
        input_filename: The cleaned input filename.
        output_filename: The processed output filename.
    Returns:
        The output data frame.
    """
    df = pd.read_csv(
        input_filename
    )
    # TODO (4) – generate a processed data frame that groups by the weekday.
    df_process.to_csv(output_filename, index=False)
    return df_process


def main():
    df = process_input()


if __name__ == "__main__":
    main()
