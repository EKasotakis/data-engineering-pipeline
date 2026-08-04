import pandas as pd

from src.transform import transform_weather_data


def test_transform_weather_data():
    raw_data = {
        "hourly": {
            "time": ["2026-08-04T00:00"],
            "temperature_2m": [20.5],
            "relative_humidity_2m": [65],
            "precipitation": [0.0],
            "wind_speed_10m": [5.2],
        }
    }

    dataframe = transform_weather_data(raw_data)

    assert isinstance(dataframe, pd.DataFrame)
    assert len(dataframe) == 1
    assert dataframe["temperature_2m"].iloc[0] == 20.5
    assert pd.api.types.is_datetime64_any_dtype(dataframe["time"])