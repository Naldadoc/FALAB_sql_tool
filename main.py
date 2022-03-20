# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#imports
import platform
import sqlite_creator
import os
#global variables
system = platform.system()
PATH = os.getcwd()
#Manage different OS
if system == 'Windows':
    separatore = '\\'
    pass
else:
    separatore = '/'
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}'.format(name=name))  # Press Ctrl+F8 to toggle the breakpoint.
    return
# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    print_hi('PyCharm run on {system} OS'.format(system=system))
    #create new db
    FALAB_DB = sqlite_creator.DB_sqlite(PATH,'FALAB_db.db',separatore)
    #create tabelle
    FALAB_DB.create_table('Analisi')
    FALAB_DB.create_table('Utenti')
    FALAB_DB.create_table('Immagini')
    FALAB_DB.create_table('Eventi')
    #Definizione colonne Utenti
    FALAB_DB.add_col('Utenti','Nome','CHAR', 'NOT NULL')
    FALAB_DB.add_col('Utenti', 'Cognome', 'CHAR', 'NOT NULL')
    FALAB_DB.add_col('Utenti', 'Password', 'CHAR', 'NOT NULL')
    FALAB_DB.add_col('Utenti', 'Privilegi', 'CHAR', 'NOT NULL')
    #inserimento utente Base
    record_base = {'Nome':'Admin','Cognome':'root','Password':'Root','Privilegi':'admin'}
    FALAB_DB.insert_record('Utenti',record_base)
    records = FALAB_DB.show_records('Utenti')
    print(records)
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
