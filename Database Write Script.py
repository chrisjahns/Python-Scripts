# Database Write Script

#%% Load Libraries
from cmath import nan
import os
import numpy as np
import pandas as pd
import pyodbc
import sqlalchemy as sa
from sqlalchemy import create_engine

# Assign Parameters
working_dir = ''

# Assign Working Dir
os.chdir(working_dir)

# Filename Prompt
print('Enter filename of data file:')
filename = str(input())

# Load Data
if filename.endswith == '.xlsx':
    df = pd.read_excel(filename, engine='openpyxl')
elif filename.endswith == '.csv':
    df = pd.read_csv(filename)

# Create Function to Determine DB Engine
def create_db_conn(df):

    # Enter database host connection information
    print('Input database host:')
    db_host = str('input()')

    # Enter database name information
    print('Input database name:')
    db_name = str(input())

    # Enter credentials
    print('Enter username:')
    u_name = str(input())

    print('Enter password:')
    p_word = str(input())

    conn = sa.engine.URL.create(
        'mssql+pyodbc',
        username=u_name,
        password=p_word,
        query={'driver':'SQL Server Native Client 11.0'},
        host=db_host,
        database=db_name
    )

    # Set SQL Engine
    global db_engine
    db_engine = create_engine(conn)
    print(db_engine)

def write_to_db(engine):
    # Define DB write parameters
    print('Define name of table to write:')
    table_name = str(input())

    print('Define schema name:')
    schema_name = str(input())

    print('Write behavior: ("fail", "replace", "append")')
    behavior = str(input())

    # Write to db
    df.to_sql(table_name, engine, schema=schema_name, if_exists=behavior)

#%% Run Create DB Connection
create_db_conn(df)

#%% Run Write to DB
write_to_db(db_engine)
