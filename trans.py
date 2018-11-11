import pandas as pd
import sqlite3

conn = sqlite3.connect('example.db')
curs = conn.cursor()

df = pd.read_csv('data.csv')

print(df.head())

df.to_sql('data', conn)