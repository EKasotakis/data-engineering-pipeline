import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_database_engine():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")

    database_url = (
        f"postgresql+psycopg2://{user}:{password}"
        f"@{host}:{port}/{database}"
    )

    engine = create_engine(database_url)

    return engine


def load_to_database(dataframe):
    engine = get_database_engine()

    dataframe.to_sql(
        "weather_data",
        con=engine,
        if_exists="append",
        index=False,
    )

    print("Data successfully loaded into PostgreSQL.")