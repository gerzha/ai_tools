from typing import List, Union

import pandas as pd
from pydantic import BaseModel



DEFAULT_COLUMNS: List[str] = [
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "volumeCcy",
        "volCcyQuote",
        "confirm",
    ]


def wrap_candlestick_data_to_pd(
    data: List[Union[list, tuple]], columns: List[str] = None
) -> pd.DataFrame:
    """
    Converts candlestick data into a pandas DataFrame.

    Parameters:
    - data (List[Union[list, tuple]]): The candlestick data to be converted.
    - columns (List[str], optional): Column names for the DataFrame.
      Defaults to CandlestickColumns.DEFAULT_COLUMNS.

    Returns:
    - pd.DataFrame: DataFrame containing the candlestick data.
    """

    # Use provided columns or default if not provided
    if columns is None:
        columns = DEFAULT_COLUMNS
    else:
        # Handle the case where provided columns are less or more than expected
        if len(columns) != len(DEFAULT_COLUMNS):
            raise ValueError(
                f"Expected {len(DEFAULT_COLUMNS)} columns, got {len(columns)}"
            )

    # Validate the format of data
    if not all(
        isinstance(row, (list, tuple)) and len(row) == len(columns) for row in data
    ):
        raise ValueError(
            "Invalid data format. Each row must match the number of columns."
        )

    df = pd.DataFrame(data, columns=columns)
    return df
