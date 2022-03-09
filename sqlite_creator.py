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
        self.db = sqlite3.connect('{path}\\{db}'.format(path=self.path,db = self.db_name))
        return

    def create_table(self,table_name,columlist):
        '''

        :param table_name: Name of table
        :param columlist: List of columns
        :return:
        '''

        return

    pass