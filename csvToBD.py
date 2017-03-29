# coding: utf-8
import csv
import sys


def openCSV(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        tab1 = []
        try:
            for row in reader:
                print(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

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



if __name__ == '__main__':
    fichierCSV = openCSV("installations_table.csv")
    print(fichierCSV)
