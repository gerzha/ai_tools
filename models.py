import re

from pydantic import BaseModel, field_validator


class OKXTimeFrame(BaseModel):
    timeframe: str

    @field_validator("timeframe")
    def validate_timeframe(cls, v):
        valid_timeframes = [
            "6Hutc",
            "12Hutc",
            "1Dutc",
            "2Dutc",
            "3Dutc",
            "1Wutc",
            "1Mutc",
            "3Mutc",
        ]
        if v not in valid_timeframes:
            raise ValueError(
                f"Invalid timeframe. Valid options are: {', '.join(valid_timeframes)}"
            )
        return v


class OKXCurrencyPair(BaseModel):
    currency_pair: str

    @field_validator("currency_pair")
    def validate_currency_pair(cls, v):
        # Regular expression for matching currency pair pattern
        pattern = r"^[A-Z]{3,4}-[A-Z]{3,4}$"
        if not re.match(pattern, v):
            raise ValueError("Invalid currency pair. Format must be 'ABC-DEF'.")
        return v
