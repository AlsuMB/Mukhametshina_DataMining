import requests
import vk_api
import psycopg2

import airflow
from airflow import DAG
import datetime
from datetime import timedelta
from airflow.operators.python import PythonOperator

from vkcrawler import vk_craw

con = psycopg2


def connectBD():
    global con
    con = psycopg2.connect(host='database-1.cj4nt3ktyazz.us-east-1.rds.amazonaws.com',
                           port='5432', user='postgres', password='postgres')


def topWords():
    un_wordsR = vk_craw('login', 'password')
    save_data(un_wordsR, con)


def save_data(un_wordsR, con):
    leng = len(un_wordsR)
    with con.cursor() as cursor:
        i = 0
        cursor.execute(f'''TRUNCATE TABLE  wordss;''')

        for w in un_wordsR:
            print(f'\r записывается {i + 1} из {leng}', end="", flush=True)
            cursor.execute(f'''INSERT INTO wordss (word, counter) VALUES('{w}',{un_wordsR[w]});''')
            i += 1

    con.commit()
    con.close()


def main():
    connectBD()
    topWords()


main()

args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2021, 3, 18),
    'retries': 1,
    'schedule_interval': '@daily',
    'retry_delay': datetime.timedelta(days=1),
    'depends_on_past': False,
}

with DAG(dag_id='FirstDag', default_args=args, schedule_interval=timedelta(days=1)) as dag:
    parse_vk = PythonOperator(
        task_id='topWordsVk',
        python_callable=main,
        dag=dag
    )
