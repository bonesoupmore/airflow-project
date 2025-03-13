import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=get_sftp,
    )
