import pandas as pd


def validate_weather_data(dataframe: pd.DataFrame) -> None:
    missing_values = dataframe.isna().sum()

    if missing_values.any():
        raise ValueError(
            f"Missing values found:\n{missing_values[missing_values > 0]}"
        )