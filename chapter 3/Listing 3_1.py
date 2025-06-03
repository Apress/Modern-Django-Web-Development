#Listing 3_1 : create table
import sqlite3

conn=sqlite3.connect("mydata.sqlite3")
cur=conn.cursor()

qry='''
CREATE TABLE IF NOT EXISTS Books (
  id INTEGER (10) PRIMARY KEY,
  title STRING (50),
  author STRING (20),
  price INTEGER (10),
  publisher STRING (20)
  );
'''

cur.execute(qry)
conn.close()