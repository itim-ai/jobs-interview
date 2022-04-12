"""Module to generate the input data."""

import numpy as np
import pandas as pd


def generate_input(
    mu: int = 100, sigma: int = 2, n: int = 102, output_filename: str = "./data/input.csv"
):
    """Generates and returns an array of Gaussian random data above a given mean
    standard deviation. The weekdays should start from 1 ... 7 and repeat.

    Args:
        mu: The mean of the data.
        sigma: The standard deviation of the data.
        n: The number of points to generate.
        output_filename: Filename to write the data to.
    Returns:
        An array of Gaussian random data above a given mean standard deviation.
    """
    ids = range(1, n + 1)
    # TODO (1) – compute the weekdays variable, i.e., weekdays = [1,2,3,4,5,6,7,1,2,3,....]
    np.random.seed(0)  # sales_quantities[0] = 104 for mu = 100 and sigma = 2
    sales_quantities = np.random.normal(loc=mu, scale=sigma, size=n).round().astype(int)
    sales_quantities[0] += 100 * sigma  # add 100-sigma amount to the first data point.
    df = pd.DataFrame({"id": ids, "weekday": weekdays, "sales_quantity": sales_quantities})
    df.to_csv(output_filename, index=False)
    return df


def main():
    df = generate_input()


if __name__ == "__main__":
    main()
