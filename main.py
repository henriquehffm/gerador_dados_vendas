#%%
from faker import Faker
from datetime import datetime, timedelta,date
import json
import boto3
from dotenv import load_dotenv
from os import getenv
from botocore import exceptions
from botocore.exceptions import ClientError
import logging
import pandas as pd


fake = Faker('pt-BR')

def gen_clientes(qtd_clientes):
    clientes = []

    for _ in range(qtd_clientes):

        cliente = {
            'client_id': fake.random_int(min=1, max=999),
            'empresa': fake.unique.company(), 
            'comprador': fake.unique.name(), 
            'telefone': fake.unique.phone_number(), 
            'estado': fake.state_abbr(),
            'cidade': fake.city()
            }
        clientes.append(cliente)

    return clientes

def gen_orcamentos(qtd_entradas, clientes):
    
    orcamentos = []

    for _ in range(qtd_entradas):

        cliente = fake.random_element(clientes)
        solicitado = fake.date_between(start_date='-390d',end_date='-35d')
        orcado = fake.date_between(start_date=solicitado + timedelta(days=1), end_date= solicitado + timedelta(days=5))
        vendido = fake.boolean()
        fechado = fake.date_between(start_date=orcado, end_date=solicitado + timedelta(days=30)) if vendido else None

        entrada = {
            'solicitado': solicitado.isoformat(),
            'orcado': orcado.isoformat(),
            'valor': fake.random_int(min=10000,max=2000000) / 100,
            'fechado': fechado.isoformat() if fechado else None ,
            **cliente
        }
        
        orcamentos.append(entrada)

    return orcamentos

def load_to_s3(object, bucket, name):
    load_dotenv('vim.env')
    s3_client = boto3.client(
        's3',
        aws_access_key_id = getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key = getenv('AWS_SECRET_ACCESS_KEY')
    )
    try:
        s3_client.create_bucket(Bucket=bucket)
    except ClientError as e:
        logging.error(e)
    
    try:
        s3_client.put_object(Body = object, Bucket = bucket, Key=name)
    except ClientError as e:
        logging.error(e)
        return False
    
    return True

# %%

clientes = gen_clientes(100)

orcamentos = gen_orcamentos(3000, clientes)

orc_id = fake.random_int(min=3000, max=50000)

orcamentos.sort(key = lambda x: x['orcado'])

for entry in orcamentos:
    entry['id'] = orc_id
    orc_id += 1

# %%
#sem particionar

str = ''

for line in orcamentos:
    str += json.dumps(line)+'\n'

load_to_s3(str.encode('utf-8'),
            bucket='hh-desafio01-howbootcamps', 
            name='orcamentos_n/orcamentos.json')

# %%
#particionado 

df = pd.DataFrame(orcamentos)
df['orcado'] = pd.to_datetime(df['orcado'])
df['PARTITION'] = df['orcado'].apply(lambda x: x.strftime("%Y-%m"))
column_values = df['PARTITION'].unique()

for value in column_values:
    filtered_df = df[df['PARTITION'] == value]

    load_to_s3(filtered_df.to_json(orient='records', lines=True),
               bucket='hh-desafio01-howbootcamps', 
               name=f'orcamentos_partitioned/YMo={value}/{value}.json')

# %%
