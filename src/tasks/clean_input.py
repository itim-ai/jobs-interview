"""Module to clean the input data."""

from typing import Tuple
import numpy as np
import pandas as pd


def mad_std(sales_quantities: np.array) -> float:
    """Calculates and returns the median absolute deviation of the sales quantities.

    Args:
        sales_quantities: An array of sales quantities.
    Returns:
        The median absolute deviation of the sales quantities.
    """
    dev = sales_quantities - np.median(sales_quantities)
    abs_dev = abs(sales_quantities - np.median(sales_quantities))
    return np.median(abs_dev) * 1.4826  # scale to the Gaussian equivalent.


def get_mu_and_sigma(df: pd.DataFrame) -> Tuple[float]:
    """Computes and returns the median and (equivalent) standard deviation of the sales
    quantities.

    Args:
        df: Data frame containing the weekdays and sales quantities.
    Returns:
        The median and equivalent standard deviation of the sales quantities.
    """
    # TODO (2) – compute the mean sales quantity.
    sigma = mad_std(df["sales_quantity"])
    return mu, sigma


def sigma_clip(
    df: pd.DataFrame, mu: float, sigma: float, n_sigma: float
) -> pd.DataFrame:
    """Clips a data frame by its sales quantity value.

    Args:
        df: The data frame to clip.
        mu: The mean sales quantities.
        sigma: The standard deviation of the sales quantities.
        n_sigma: The number of sigma above the mean to clip.
    Returns:
        The sigma-clipped data frame.
    """
    df_clipped = df.copy()
    df_clipped = df_clipped[abs(df_clipped["sales_quantity"] - mu) < n_sigma * sigma]
    return df_clipped


def clean_input(input_filename: str = "./data/input.csv", output_filename: str = "./data/input-cleaned.csv") -> pd.DataFrame:
    """Cleans the raw input (containing the weekday and corresponding sales quantity).

    Args:
        input_filename: The input filename.
        output_filename: The output filename.
    Returns:
        The cleaned input data frame.
    """
    df = pd.read_csv(input_filename)
    stats = get_mu_and_sigma(df)
    # TODO (3) – convert stats[0] to an integer.
    df_clean = sigma_clip(df, mu=stats[0], sigma=stats[1], n_sigma=5.0)
    df_clean.to_csv(output_filename, index=False)
    return df_clean


def main():
    df_clean = clean_input()


if __name__ == "__main__":
    main()
