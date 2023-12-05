import okx.MarketData as Market
import pandas as pd
from binance.client import Client

from models import OKXCurrencyPair, OKXTimeFrame
from wrappers import wrap_candlestick_data_to_pd


class OkxClient:
    """
    A client class for interacting with the OKX API.

    This class provides methods to fetch candlestick data from OKX.
    Candlestick data is used for understanding market trends in cryptocurrency trading.

    Documentation: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-candlesticks
    """

    def __init__(self):
        self.client = Market.MarketAPI()

    def get_candles(
        self,
        currency_pair: OKXCurrencyPair = OKXCurrencyPair(
            currency_pair="BTC-USDT"
        ).currency_pair,
        timeframe: OKXTimeFrame = OKXTimeFrame(timeframe="1Dutc").timeframe,
        period: int = 100,
    ) -> pd.DataFrame:
        """
        Fetches candlestick data for a specified currency pair and timeframe from the OKX API.

        Parameters:
        - currency_pair (OKXCurrencyPair): The trading pair to fetch data for, e.g., BTC-USDT.
        - timeframe (OKXTimeFrame): The timeframe for the candlestick data, e.g., 1Dutc.
        - period (int): The number of data points to fetch.

        Returns:
        - Candlestick data as specified by the currency pair and timeframe.

        Raises:
        - ValidationError: If the input parameters are not valid.
        """
        response = self.client.get_candlesticks(
            instId=currency_pair, bar=timeframe, limit=period
        )
        return wrap_candlestick_data_to_pd(data=response["data"])


class BinanceClient:
    def __init__(self):
        self.client = Client()
