'''
=================================================
Milestone 3

Nama  : Muhammad iqbal
Batch : FTDS-040-RMT

Program ini dibuat untuk melakukan automatisasi data cleaning dengan mengambil data dari postgresql.
Adapun dataset yang dipakai adalah dataset mengenai performa pengiriman jasa pesan antar platform luar negeri.
=================================================
'''

import pandas as pd
import psycopg2 as db
import os

from airflow.models import DAG

from airflow.operators.python import PythonOperator
from elasticsearch import Elasticsearch

from datetime import datetime, timedelta

default_args= {
    'owner': 'iqbal',
    'start_date': datetime(2024, 11, 1) - timedelta(hours=7),
}

def save_files(df_list):
    '''
    accepts dataframe list as input
    saves each dataframe in the tmp folder as csv
    the file name corresponds to the dataframe "name" attribute
    '''
    [ df.to_csv('/opt/airflow/dags/' + df.name + '.csv' , sep=',', index=False) for df in df_list ]



def load_files(names_list):
    '''
    accepts a list of names (str) as input
    load each csv file from the tmp folder with the input names
    returns a list of loaded dataframes
    '''
    df_list = []
    [ df_list.append(pd.read_csv("/opt/airflow/dags/" + name + ".csv")) for name in names_list if os.path.isfile('/opt/airflow/dags/' + name + '.csv') ]

    return df_list

def dataLoading():
    '''
    Fungsi ini untuk load data dari postgresql
    
    '''
    conn_string="dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432' "
    conn=db.connect(conn_string)
    df=pd.read_sql("select * from table_m3", conn)
    df.name ="P2M3_muhammad_iqbal_data_raw"
    conn.close()
    save_files([df])
    
def dataCleaning():
    
    ''' 
    Fungsi untuk data cleaning dengan data yg diambil dari server postgresql
    
    Argument:
    None
    
    Output:
    P2M3_muhammad_iqbal_data_clean.csv
    '''
    # Preprocessing
    df = load_files(['P2M3_muhammad_iqbal_data_raw'])[0]
    df.drop_duplicates(inplace=True)
    df.columns = [col.lower() for col in df.columns]
    df.columns = df.columns.str.replace(" ", "_")
    df.rename(columns={"delivery_time_(minutes)":"delivery_time_minutes", "order_value_(inr)":"order_value_inr"}, inplace=True)
    df["order_date_&_time"] = pd.to_datetime(df["order_date_&_time"], format="%M:%S.%f")
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Save data
    df.name ="P2M3_muhammad_iqbal_data_clean"
    save_files([df])
    print("-------Data Saved------")

def postToElastic():
    '''
    Fungsi ini untuk post dataset yg sudah di preprocess ke elasticsearch
    
    '''
    es = Elasticsearch("elasticsearch:9200")
    df = load_files(['P2M3_muhammad_iqbal_data_clean'])[0]
    for i,r in df.iterrows():
        doc=r.to_json()
        res=es.index(index="frompostgresql", doc_type="doc", body=doc)
        print(res)


with DAG(
    "Project_milestone3_iqbal",
    description='End to end data engineering project',
    schedule_interval='10-30/10 9 * * sat',
    default_args=default_args, 
    catchup=False) as dag:

   # Task : 1
    load_data = PythonOperator(
        task_id="data_loading",
        python_callable = dataLoading
    )
   
    # Task : 2
    clean_data = PythonOperator(
        task_id="data_cleaning",
        python_callable = dataCleaning
    )

    # Task : 3
    post_to_elasticsearch = PythonOperator(
        task_id="post_to_elasticsearch",
        python_callable = postToElastic
    )
    
load_data >> clean_data >> post_to_elasticsearch