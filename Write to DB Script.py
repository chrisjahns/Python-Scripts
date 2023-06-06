# Write to DB

#%% Load Libraries
import os
import numpy as np
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine

# Assign Working Directory
working_dir = ''

# Change Working Directory
os.chdir(working_dir)
print(os.getcwd())

# Enter Filename of Data
print('Enter Filename of Data: ')
filename = str(input())
print(filename)

# Load Data
if filename.endswith == '.xlsx':
    df = pd.read_excel(filename, engine='openpyxl')
elif filename.endswith == '.csv':
    df = pd.read_csv(filename)

df = pd.read_csv(filename)
print(df.head())

# Create Function to Determine DB Engine
def create_db_conn(df):
    # Enter Database Connection
    print('Choose Database Connection: (Production or Public')
    db_conn = str(input())

    # Input Database Credentials
    print('Enter username: ')
    u_name = str(input())

    print('Enter password: ')
    p_word = str(input())

    #%% Define DB Connection
    if db_conn == 'Production':
        conn = sa.engine.URL.create(
            'mssql+pyodbc',
            username= u_name,
            password= p_word,
            query={'driver':'SQL Server Native Client 11.0'},
            host='',
            database='',
        )

    elif db_conn == 'Public':
        conn = sa.engine.URL.create(
            'mssql+pyodbc',
            username=u_name,
            password=p_word,
            query={'driver':'SQL Server Native Client 11.0'},
            host='',
            database='',
        )

    # Set SQL Engine
    global db_engine
    db_engine = create_engine(conn)
    print(db_engine)

def write_to_db(engine):
    # Determine DB Write Commands
    print('Define Name of Table to Write:')
    table_name = str(input())
    print(table_name)

    print('Define schema name:')
    schema_name = str(input())
    print(schema_name)

    print('Write Behavior: ("fail", "replace", "append")')
    behavior = str(input())
    print(behavior)

    #%% Write to DB
    df.to_sql(table_name, engine, schema=schema_name, if_exists=behavior)
    

#%% Run Functions
create_db_conn(df)
#%%
write_to_db(db_engine)
#%%
