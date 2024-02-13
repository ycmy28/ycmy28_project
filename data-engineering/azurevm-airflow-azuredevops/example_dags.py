import pyodbc
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.hooks.base_hook import BaseHook
import pendulum

def my_function():
    # Retrieve the connection information
    conn_info = BaseHook.get_connection("")
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={conn_info.host};DATABASE={conn_info.schema};UID={conn_info.login};PWD={conn_info.password}'

    # Establish a connection using the connection string
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Perform some operations
    cursor.execute("SELECT TOP 1 * FROM your_table")
    row = cursor.fetchone()
    print(row)

    # Close the connection
    conn.close()

def test_sql_server_connection():
    import pandas as pd
    try:
        server_name = ''
        database_name = ''
        username = ''
        password = ""
        # Create a connection string
        connection_string = f'DRIVER=SQL Server Native Client 11.0;SERVER={server_name};DATABASE={database_name};UID={username};PWD={password}'
        
        # Establish the connection
        conn = pyodbc.connect(connection_string)
        query = "SELECT TOP (1000) * FROM [dbo].[DummyTable]"
        df_sql = pd.read_sql_query(query, conn)
        conn.close()
        
        #return conn
        return print(df_sql)
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

with DAG(
    'dag_test_connection',
    default_args={
        'depends_on_past': False,
        'email': 'email@somewhere.com',
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=1),
        'sla': timedelta(minutes=30),
        'weight_rule': 'absolute',
    },
    catchup=False,
    description='DAG Test',
    schedule_interval='@daily',
    start_date=datetime(2023, 3, 28, 0, 0, 0, tzinfo=pendulum.timezone('Asia/Jakarta')),
    #template_searchpath='',
    tags=['dag_test'],
    render_template_as_native_obj=True,
    is_paused_upon_creation=True,
) as dag:
    task = PythonOperator(
    task_id='run_query',
    python_callable=test_sql_server_connection
    )
    
    my_task = PythonOperator(
    task_id='my_task',
    python_callable=my_function
    )
    
    task >> my_task