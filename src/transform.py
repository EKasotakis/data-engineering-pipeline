import pandas as pd


def transform_weather_data(raw_data: dict) -> pd.DataFrame:
    hourly_data = raw_data["hourly"]

    dataframe = pd.DataFrame(hourly_data)

    dataframe["time"] = pd.to_datetime(dataframe["time"])

    print(dataframe.isna().sum())

    return dataframe