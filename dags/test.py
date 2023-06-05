from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_hello():
    print("Hello!")


def print_goodbye():
    print("Goodbye!")


def print_airflow():
    print("Airflow!")


dag = DAG("test_dag", start_date=datetime(2023, 6, 4))

t1 = PythonOperator(task_id="print_hello", python_callable=print_hello, dag=dag)
t2 = PythonOperator(task_id="print_goodbye", python_callable=print_goodbye, dag=dag)
t3 = PythonOperator(task_id="print_airflow", python_callable=print_airflow, dag=dag)

t1 >> t2 >> t3
