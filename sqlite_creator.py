'''
This file is a general purpose sqplite db manipulation
'''

import sqlite3

class DB_sqlite():
    def __init__(self,path_db, db_name):
        '''

        :param path_db: path where db will be created type STRING
        :param db_name: name of database type STRING
        '''
        self.path = path_db
        self.name = db_name
        db = sqlite3.connect('{path}\\{db}'.format(path=self.path,db = self.db_name))
        db.close()
        return

    def create_table(self,table_name):
        '''

        :param table_name: Name of table
        :param columlist: List of columns
        :return:
        '''
        # Connessione al Database
        db = sqlite3.connect('{path}\\{db}'.format(path=self.path,db = self.db_name))
        #creazione del cursore
        cursor_db = self.db.cursor()
        #esecuzione comando
        cursor_db.execute("CREATE TABLE IF NOT EXISTS {name_tab} (id int NOT NULL PRIMARY KEY AUTO_INCREMENT)".format(
            name_tab=table_name))
        # Disconnessione dal DB
        db.close()
        return

    def add_col(self,table,name,type,spec):
        '''

        :param name: Nome colonna
        :param type: Tipo dato
        :param spec: Specifica colonna
        La funzione aggiunge una colonna alla tabella di riferimento
        :return result: string of execution
        '''

        # Connessione al Database
        db = sqlite3.connect('{path}\\{db}'.format(path=self.path,db = self.db_name))
        #creazione del cursore
        cursor_db = self.db.cursor()
        #esecuzione comando
        cursor_db.execute("ALTER TABLE IF EXISTS {table} ADD {col_name} {data_type} {spec}".format(table=table,
        col_name=name, data_type=type, spec=spec))
        # Disconnessione dal DB
        db.close()
        result = 'Column' + name + ' added'
        return result

    def insert_record(self,table,record):
        return

    def change_record(self,table,loc,record):
        return
    def delete_record(self,table,loc,record):
        return
    pass