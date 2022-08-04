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
        cursor_db.execute("CREATE TABLE IF NOT EXISTS {name_tab} (id INTEGER PRIMARY KEY)".format(
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
        col = self.retrieve_col(table)
        if col.__contains__(name):

            result = 'Column {name} already present'.format(name=name)

            pass
        else:

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
            pass

        return result

    def retrieve_col(self, table):
        '''

        :param table: Nome Tabella
        :return: Ritorna la lista delle colonne della tabella
        '''
        column = list()
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        # Ricerca colonne nomi
        data = cursor_db.execute("SELECT * FROM {table}".format(table=table))
        for col in data.description:
            column.append(col[0])
            pass
        # Disconnessione dal DB
        db.close()

        return column

    def insert_record(self,table,record):
        '''
        La funzione agginge un record ad una tabella
        :param table: Nome tabella
        :param record: Dictonary based on column name
        :return:
        '''
        columns = ''
        values = []
        # Creazione stringa SQL
        for i in record.keys():
            if i == 'id':
                pass
            else:
                if columns == '':
                    columns = i
                    pass
                else:
                    columns = columns + ',' + ' ' + i
                    pass

                values.append(record[i])
                pass
            pass
        values = tuple(values)
        sql = "INSERT INTO {table} ({columns}) VALUES {values}".format(table=table,columns=columns,values=values)
        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        # esecuzione comando inserimento valore
        cursor_db.execute(sql)
        db.commit()
        # Disconnessione dal DB
        db.close()
        return

    def change_record(self,table,loc,record):
        '''
        La funzione modifica un record esistente nella tabella selezionata
        :param table: Nome Tabella type STRING
        :param loc: indice della tabella da modificare type INT
        :param record: Lista dei nuovi parametri type Dict()
        :return:
        '''
        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        for i in record.keys():
            value = record[i]
            if type(value) is str:
                value = '\''+value+'\''
                pass
            sql = "UPDATE {table} SET {column} = {value} WHERE {table}.id = {loc}".format(table=table,
                                                                                      column=i,
                                                                                      value=value,
                                                                                      loc=loc)
            cursor_db.execute(sql)
            pass
        #esecuzione comando
        db.commit()
        # Disconnessione dal DB
        db.close()
        return

    def delete_record(self,table,loc):
        '''
        La funzione cancella un record della tabella
        :param table: Nome tabella type STRING
        :param loc: Indice record da eliminare type INT
        :return:
        '''

        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        #esecuzione comando
        cursor_db.execute('DELETE FROM {table} WHERE {table}.id = {loc}'.format(table=table,loc=loc))
        db.commit()
        # Disconnessione dal DB
        db.close()
        return

    def show_records(self,table,loc=0, col = '*', ):
        '''
        :param loc: indice da visualizzare di defaul 0
        :param table: Nome tabella type STRING
        :param col: Nome della colonna da estrarre (tutte di default)
        :return: tabella completa
        '''
        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        out =[]
        #SQL command
        if loc == 0:

            cursor_db.execute('SELECT * FROM {table}'.format(table=table))
            list = cursor_db.fetchall()
            pass
        else:
            for i in loc:
                cursor_db.execute('SELECT {col} FROM {table} WHERE {table}.id = {loc}'.format(table=table,loc=i,col = col))
                list = cursor_db.fetchall()
                pass
            pass
        db.close()
        for i in list:
            out.append(i[0])
            pass
        return out

    def search_loc(self, table, col, condition):
        '''

        :param table: tabella in cui eseguire la ricerca type: STRING
        :param col: colonna su cui eseguire la ricerca
        :param condition: Condizione di ricerca - type:String
        :return loc: Lista degli indici che corrispondono alla condizione type: list
        '''
        loc = []
        # Connessione al Database
        db = sqlite3.connect('{path}{separatore}{db}'.format(path=self.path,separatore=self.separatore,db = self.db_name))
        #creazione del cursore
        cursor_db = db.cursor()
        # Esecuzione comando di ricerca
        cursor_db.execute('SELECT {table}.id FROM {table} WHERE {table}.{col} = \'{condition}\''.format(table = table, col = col, condition = condition))
        out = cursor_db.fetchall()
        db.close()
        # Crazione della lista delle posizioni
        for i in out:
            loc.append(i[0])
            pass
        return loc
    pass