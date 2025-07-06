"""A DAG ETL pipeline geocode from locationiq"""

from datetime import datetime, timedelta
import os, sys

from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
import logging

from src.transformers.address_transformer import transform as tfm
from src.utils.reader import read_json
from src.utils.writer import write_enriched_data

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_KEY = Variable.get("LOCATIONIQ_KEY")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="geocode_pipeline",
    default_args=default_args,
    description='DAG ETL Pipeline geocode from json data to output as json with locationiq',
    start_date=datetime(2025, 7, 1),
    schedule_interval=None,
    catchup=False,
    tags=["geocode", "etl"],
) as dag:

    start = EmptyOperator(task_id="start")

    with TaskGroup("ETL_task", tooltip="extract→transform→load") as etl_group:
        @task
        def extract():
            return list(read_json(os.path.join("data", "int_test_input")))

        # @task
        # def transform(records: list):
        #     out = []
        #     for rec in records:
        #         addr = rec.get("project_address", "").strip()
        #         geo = get_structured_address(addr, API_KEY)
        #         rec.update(geo)
        #         out.append(rec)
        #     return out
        @task(retries=3, retry_delay=timedelta(seconds=30))
        def transform(records: list) -> list:
            return tfm(iter(records), API_KEY)

        @task
        def load(enriched: list):
            write_enriched_data(iter(enriched), os.path.join("data", "int_test_output"))

        # TaskGroup
        extracted = extract()
        transformed = transform(extracted)
        loaded    = load(transformed)

    completion = EmptyOperator(task_id="all_task_complete")

    # graph definition
    start >> etl_group >> completion
