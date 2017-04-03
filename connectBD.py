import os
import sqlite3
import csv
from csvToBD import *
# import mysql.connector

# Lire le fichier CSV
def openCSV(file):
    with open(file, 'r', encoding='utf_8') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        # head = []
        sqllist = []

        try:
            for elem in header:
                #Pour les noms des attributs, nous avons remplace ' ' par '_' ,"'" par  ""
                head = [elem][0].replace(' ', '_').replace("'", "")
                sqllist.append("{} VARCHAR (50)".format(head))
            return sqllist

            for row in reader:
            rows = tab[row]
            # print (row)
        except csv.Error as e:
            # sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
            print(e)
            return

            # with open(file,newline = '') as r:
            #     reader = csv.DictReader(r)
            #     header = reader.fieldnames
            #     # nous avons créé une matrice pour stocker les éléments dans la base des données
            #     tab1 = []
            #     tab2 = []
            #     for row in reader:
            #         for element in header:
            #             tab2.append(row[element])
            #         tab1.append(tab2)
            #         tab2=[]
            #     return tab1



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

# Connexion sqlite3
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    if os.path.exists(DB_PATH) and os.path.isfile(DB_PATH):
        return conn


# Deconnexion
def close_all(cu):
    cu.close()


# get_cursor
def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn().cursor()


def sqlCreateTable(sqlcom):
    con = get_conn()
    cur = get_cursor(con)
    sql1 = 'CREATE TABLE {} ({});'.format(DB_PATH.replace(".db", ''), "id int")
    cur.execute(sql1)
    con.commit()
    close_all(con)
    for i in sqlcom:
        try:
            con = get_conn()
            cur = get_cursor(con)
            sql1 = 'ALTER TABLE {} ADD {}'.format(DB_PATH.replace(".db", ''), i)
            cur.execute(sql1)
            con.commit()
            close_all(con)
        except Exception as e:
            print(e)
        finally:
            close_all(con)

def insertionTable():
    try:
        con = get_conn()
        cur = get_cursor(con)
        data = ..
        sqlInsert='INSERT INTO TABLE {} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        cur.execute(sqlInsertm, .. )
    except Exception as e:
        print(e)
    finally:
        close_all(con)




if __name__ == '__main__':
    file_name = 'equipements_activites.csv'#Nom fichier
    DB_PATH=file_name.replace("csv","db")#Nom creation db(si il n'existe pas,create)
    sqlCreateTable(openCSV(file_name))
