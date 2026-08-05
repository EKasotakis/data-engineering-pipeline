import pandas as pd
import streamlit as st
import plotly.express as px

from src.load import get_database_engine

st.title("Luxembourg Weather Dashboard")

engine = get_database_engine()

query = """
SELECT *
FROM weather_data
ORDER BY time;
"""

dataframe = pd.read_sql(query, engine)

st.sidebar.header("Filters")

selected_days = st.sidebar.slider(
    "Number of days",
    min_value=1,
    max_value=4,
    value=4,
)

latest_time = dataframe["time"].max()

filtered_dataframe = dataframe[
    dataframe["time"] >= latest_time - pd.Timedelta(days=selected_days)
]

# ← Add the statistics HERE
st.subheader("Current Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Temperature (°C)",
    round(filtered_dataframe["temperature_2m"].mean(), 1),
)

col2.metric(
    "Average Humidity (%)",
    round(filtered_dataframe["relative_humidity_2m"].mean(), 1),
)

col3.metric(
    "Average Wind Speed (km/h)",
    round(filtered_dataframe["wind_speed_10m"].mean(), 1),
)

temperature_chart = px.line(
    filtered_dataframe,
    x="time",
    y="temperature_2m",
    title="Temperature Over Time",
    labels={
        "time": "Time",
        "temperature_2m": "Temperature (°C)",
    },
)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.plotly_chart(
        temperature_chart,
        use_container_width=True,
    )

humidity_chart = px.line(
    filtered_dataframe,
    x="time",
    y="relative_humidity_2m",
    title="Humidity Over Time",
    labels={
        "time": "Time",
        "relative_humidity_2m": "Humidity (%)",
    },
)

with chart_col2:
    st.plotly_chart(
        humidity_chart,
        use_container_width=True,
    )


wind_chart = px.line(
    filtered_dataframe,
    x="time",
    y="wind_speed_10m",
    title="Wind Speed Over Time",
    labels={
        "time": "Time",
        "wind_speed_10m": "Wind Speed (km/h)",
    },
)

st.plotly_chart(
    wind_chart,
    use_container_width=True,
)

# ← Then display the table
st.dataframe(filtered_dataframe)