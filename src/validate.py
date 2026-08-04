import pandas as pd
import pandera.pandas as pa
from pandera.typing import Series


class WeatherSchema(pa.DataFrameModel):
    time: Series[pd.Timestamp]

    temperature_2m: Series[float] = pa.Field(
        ge=-60,
        le=60,
    )

    relative_humidity_2m: Series[int] = pa.Field(
        ge=0,
        le=100,
    )

    precipitation: Series[float] = pa.Field(
        ge=0,
    )

    wind_speed_10m: Series[float] = pa.Field(
        ge=0,
    )

    class Config:
        strict = True
        coerce = True


def validate_weather_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    if dataframe.empty:
        raise ValueError("The weather dataset is empty.")

    validated_dataframe = WeatherSchema.validate(dataframe)

    return validated_dataframe