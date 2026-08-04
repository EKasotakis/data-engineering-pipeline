import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import MetaData, Table
from src.logger import get_logger

logger = get_logger(__name__)


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

    records = dataframe.to_dict(orient="records")

    metadata = MetaData()

    weather_table = Table(
        "weather_data",
        metadata,
        autoload_with=engine,
    )

    insert_statement = insert(weather_table).values(records)

    upsert_statement = insert_statement.on_conflict_do_update(
        index_elements=["time"],
        set_={
            "temperature_2m": insert_statement.excluded.temperature_2m,
            "relative_humidity_2m": insert_statement.excluded.relative_humidity_2m,
            "precipitation": insert_statement.excluded.precipitation,
            "wind_speed_10m": insert_statement.excluded.wind_speed_10m,
        },
    )

    with engine.begin() as connection:
        connection.execute(upsert_statement)

    logger.info(
    "Loaded or updated %s rows in PostgreSQL.",
    len(records),
)

