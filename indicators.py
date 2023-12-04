import pandas as pd
import talib as ta


def rsi(data: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calculates the Relative Strength Index (RSI) of a given DataFrame.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the stock's closing prices.
    - period (int, optional): The number of periods to use for RSI calculation. Default is 14.

    Returns:
    - pd.Series: A Series containing the RSI values.

    Raises:
    - ValueError: If the required 'close' column is missing from the DataFrame.
    """

    if "close" not in data.columns:
        raise ValueError("DataFrame must contain a 'close' column.")

    # Optional: Handle or report missing data in 'close' column
    if data["close"].isna().any():
        raise ValueError("Missing data detected in 'close' column.")

    return ta.RSI(data["close"], timeperiod=period)
