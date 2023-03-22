import sqlite3 as sql
import pandas as pd
import re
import csv
connect_str = 'database.db'


def load_file(file, table):
    db = sql.connect(connect_str)
    pd.read_csv(f'{file}').to_sql(name=table, con=db, if_exists='append', index=False)


def domain(url):
    return re.search("((?<=http:\/\/)|(?<=https:\/\/)).+?(?=\/)", str(url)).group(0)


def ctas(table, query):
    db = sql.connect(connect_str)
    db.create_function("domain_of_url", 1, domain)
    db.execute("CREATE TABLE IF NOT EXISTS " + table + " AS " + query)


def save(file, table):
    db = sql.connect(connect_str)
    df = pd.read_sql_query("SELECT * FROM " + table, db)
    df.to_csv(file + ".csv", index=False)


def run_sql(query):
    db = sql.connect(connect_str)
    db.execute(query)
    db.commit()
