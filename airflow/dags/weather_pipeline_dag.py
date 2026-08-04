import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="weather_pipeline",
    start_date=pendulum.datetime(2026, 8, 1,tz="Europe/Luxembourg"),
    schedule="0 6 * * *",
    catchup=False,
    tags=["weather", "etl"],
) as dag:

    run_pipeline = BashOperator(
        task_id="run_weather_pipeline",
        bash_command=(
    "cd /opt/airflow/project && "
    "POSTGRES_HOST=host.docker.internal "
    "python main.py"
),
    )