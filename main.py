from clients import OkxClient
from indicators import rsi

if __name__ == "__main__":
    candle_data = OkxClient().get_candles()
    rsi_indicator = rsi(data=candle_data)
    print(rsi_indicator)