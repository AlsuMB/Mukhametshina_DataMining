import psycopg2

from airflow import DAG
import datetime
from datetime import timedelta
from airflow.operators.python import PythonOperator
import re

from vkcrawler import vk_craw

con = psycopg2


def connectBD():
    global con
    con = psycopg2.connect(host='database-1.cj4nt3ktyazz.us-east-1.rds.amazonaws.com',
                           port='5432', user='postgres', password='postgres')
    return con


def start():
    c = connectBD()
    words = vk_craw('login', 'password')
    save_data(words, c)


def save_data(words, con):
    leng = len(words)
    with con.cursor() as cursor:
        i = 0
        cursor.execute(f'TRUNCATE TABLE  words;')
        for key in words.keys():
            print(f'\r записывается {i + 1} из {leng}', end="", flush=True)
            word = '\'' + deEmojify(key) + '\''
            cursor.execute(f"INSERT INTO words (word, counter) VALUES({word},{words[key]});")
            i += 1

    con.commit()
    con.close()


def main():
    start()


main()

args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2021, 3, 18),
    'retries': 1,
    'schedule_interval': '@daily',
    'retry_delay': datetime.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(dag_id='FirstDag', default_args=args, schedule_interval=timedelta(days=1)) as dag:
    parse_vk = PythonOperator(
        task_id='unique_words_in_vk',
        python_callable=main,
        dag=dag
    )
