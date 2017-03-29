# import mysql.connector
from csvToBD import *
import csv
import sys
import sqlite3
import os
import glob


# from mysql.connector import errorcode


# def connectDB(host,database,user,password):
#     try:
#         cnx = mysql.connector.connect(host=host,
#         database=database,
#         user=user,
#         password=password
#         )
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#     else:
#             cnx.close()

def createDB(file):
    conn = sqlite3.connect(file)
    conn.text_factory = str
    c = conn.cursor()

    with open("installations_table.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if header:
                header = False
                sql = "DROP TABLE IF EXISTS %s" % tablename
                c.execute(sql)
                print(sql)
                sql = "CREATE TABLE %s (%s)" % (tablename, ", ".join([ "%s text" % column for column in row ]))
                c.execute(sql)
                for column in row:
                    if column.lower().endswith("_id"):
                        index = "%s__%s" % ( tablename, column )
                        sql = "CREATE INDEX %s on %s (%s)" % ( index, tablename, column )
                        c.execute(sql)
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename,", ".join([ "?" for column in row ]))
                rowlen = len(row)
            else:
                    if len(row) == rowlen:
                        c.execute(insertsql, row)
            conn.commit()
    c.close()
    conn.close()

if __name__ == '__main__':
    createDB("test.db")
