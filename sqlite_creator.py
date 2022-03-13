'''
This file is a general purpose sqplite db manipulation
'''

import sqlite3

class DB_sqlite():
    def __init__(self,path_db, db_name, separatore):
        '''

        :param path_db: path where db will be created type STRING
        :param db_name: name of database type STRING
        '''
        self.path = path_db
        self.db_name = db_name
        self.separatore = separatore
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        db.close()
        return

    def create_table(self,table_name):
        '''

        :param table_name: Name of table
        :param columlist: List of columns
        :return:
        '''
        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        #esecuzione comando
        cursor_db.execute("CREATE TABLE IF NOT EXISTS {name_tab} (id int AUTO_INCREMENT,PRIMARY KEY (id))".format(
            name_tab=table_name))
        db.commit()
        # Disconnessione dal DB
        db.close()
        return

    def add_col(self,table,name,type,spec=None):
        '''

        :param name: Nome colonna
        :param type: Tipo dato
        :param spec: Specifica colonna
        La funzione aggiunge una colonna alla tabella di riferimento
        :return result: string of execution
        '''

        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        #esecuzione comando
        cursor_db.execute("ALTER TABLE {table} ADD {col_name} {data_type} {spec}".format(table=table,
        col_name=name, data_type=type, spec=spec))
        db.commit()
        # Disconnessione dal DB
        db.close()
        result = 'Column' + name + ' added'
        return result

    def retrieve_col(self, table):
        '''

        :param table: Nome Tabella
        :return: Ritorna la lista delle colonne della tabella
        '''
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        #Sanity check
        cursor_db.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {table}".format(table=table))
        columns = cursor_db.fetchall()
        # Disconnessione dal DB
        db.close()

        return columns

    def insert_record(self,table,record):
        '''

        :param table:
        :param record: Dictonary based on column name
        :return:
        '''

        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        #Sanity check
        cursor_db.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {table}".format(table=table))
        columns = cursor_db.fetchall()
        #esecuzione comando inserimento valore
        #cursor_db.execute("")
        # Disconnessione dal DB
        db.close()
        return

    def change_record(self,table,loc,record):
        '''
        La funzione modifica un record esistente nella tabella selezionata
        :param table:
        :param loc:
        :param record:
        :return:
        '''
        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        #esecuzione comando
        cursor_db.execute("INSERT INTO {table} VALUES ({values})".format(table = table,values='string_value'))
        db.commit()
        # Disconnessione dal DB
        db.close()
        result = 'Column'
        return result

    def delete_record(self,table,loc,record):
        '''
        :param table:
        :param loc:
        :param record:
        :return:
        '''

        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = self.db.cursor()
        #esecuzione comando
        cursor_db.execute('Delete record statement')
        db.commit()
        # Disconnessione dal DB
        db.close()
        return
    pass