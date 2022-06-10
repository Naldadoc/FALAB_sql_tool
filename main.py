# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#imports
import platform
import sqlite_creator
import os
import kivy
from kivymd.app import MDApp


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

class FALAB_DatabaseApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Yellow'
        self.theme_cls.theme_style = 'Dark'
        return
    pass

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}'.format(name=name))  # Press Ctrl+F8 to toggle the breakpoint.
    return
# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    print_hi('PyCharm run on {system} OS'.format(system=system))
    # create new db
    FALAB_DB = sqlite_creator.DB_sqlite(PATH,'FALAB_db.db',separatore)
    # create tabelle
    FALAB_DB.create_table('Analisi')
    FALAB_DB.create_table('Category')
    FALAB_DB.create_table('Utenti')
    FALAB_DB.create_table('Immagini')
    FALAB_DB.create_table('Eventi')
    # Definizione colonne Utenti
    FALAB_DB.add_col('Utenti','Nome','CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Cognome', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Username', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Password', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Privilegi', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')

    # Definizione colonne Analisi
    FALAB_DB.add_col('Analisi','Data','DATETIME')
    FALAB_DB.add_col('Analisi', 'Care', 'INT','NOT NULL DEFAULT \'00000000\'')
    FALAB_DB.add_col('Analisi', '\'Part Number\'', 'CHAR')
    FALAB_DB.add_col('Analisi', '\'Serial Number\'', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    # Definizione colonne Category
    # Definizione colonne Immagini
    # Definizione colonne Eventi

    # Inserimento utente Base
    record_base = {'Nome':'Admin','Cognome':'root','Username':'admin','Password':'Root','Privilegi':'admin'}
    l = FALAB_DB.search_loc('Utenti', 'Nome', 'Admin')
    if not l:
        FALAB_DB.insert_record('Utenti', record_base)
        pass
    records = FALAB_DB.show_records('Utenti')
    print(records)
    FALAB_DatabaseApp().run()
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
