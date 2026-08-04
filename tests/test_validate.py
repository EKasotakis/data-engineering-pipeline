import pandas as pd
import pytest
import pandera as pa

from src.validate import validate_weather_data


def test_validate_weather_data_rejects_missing_values():
    dataframe = pd.DataFrame(
        {
            "time": [pd.Timestamp("2026-08-04 00:00:00")],
            "temperature_2m": [None],
            "relative_humidity_2m": [65],
            "precipitation": [0.0],
            "wind_speed_10m": [5.2],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        validate_weather_data(dataframe)

def test_validate_weather_data_rejects_invalid_humidity():
    dataframe = pd.DataFrame(
        {
            "time": [pd.Timestamp("2026-08-04 00:00:00")],
            "temperature_2m": [20.5],
            "relative_humidity_2m": [150],
            "precipitation": [0.0],
            "wind_speed_10m": [5.2],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        validate_weather_data(dataframe)