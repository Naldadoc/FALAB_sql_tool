# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#imports
import platform
import sqlite_creator
import os
from kivy.lang import Builder
from kivy.properties import StringProperty,ListProperty,ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineIconListItem


# global variables
system = platform.system()
PATH = os.getcwd()

# Manage different OS
if system == 'Windows':
    separatore = '\\'
    pass
else:
    separatore = '/'
    pass

SQL_DB = sqlite_creator.DB_sqlite(PATH,'SQL_db.db',separatore)



class SQL_DatabaseApp(MDApp):
    privilege = StringProperty()
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'BlueGray'
        self.theme_cls.theme_style = 'Light'
        self.title = 'SQL_Tool'
        Builder.load_file("Userinterface.kv")
        Builder.load_file("BaseTitleBar.kv")
        Builder.load_file("New_user.kv")
        Builder.load_file("Logged_in_interface.kv")
        Builder.load_file("Log_in_screen.kv")
        Builder.load_file("NavDrawerContent.kv")
        return UserInterface()

    def Log_in(self, username, password):
        '''
        Esegue il log in del programma
        :return:
        '''
        user_loc = int()
        pass_check = bool()
        user_data = []
        self.root.ids.root_screen.get_screen('Log_in_Screen').ids.Username_input.text = ''
        self.root.ids.root_screen.get_screen('Log_in_Screen').ids.Password_input.text = ''
        self.root.ids.root_screen.get_screen('Log_in_Screen').ids.info_label.text = ''
        user_loc = SQL_DB.search_loc('Utenti','Username',username)
        if user_loc !=[]:
            user_data = SQL_DB.show_records('Utenti', user_loc, "Privilegi")
            pass
        if user_data != []:

            self.privilege = user_data[0]
            self.root.ids.root_screen.current = 'Logged_in_interface'
            pass
        else:
            self.root.ids.root_screen.get_screen('Log_in_Screen').ids.info_label.text = 'Wrong username or password'
            pass

        return

    def add_user(self,nome,cognome,username,email,password,privilegi):
        '''
        Aggiunge il nuovo utente al database
        :return:
        '''
        return

    def set_screen(self, next_scr):

        self.prev_screen = self.root.ids.root_screen.current
        self.root.ids.root_screen.current = next_scr
        print("old:{x} and new: {y}".format(x = self.prev_screen,y=next_scr))
        return
    pass


class UserInterface(BoxLayout):
    pass


class BaseTitleBar(MDToolbar):
    root_screen = ObjectProperty()
    nav_drw = ObjectProperty()
    md_list = ObjectProperty()

    def set_elements(self,current_screen):
        '''

        :param current_screen: The current active screen
        :return:
        The function change the Toolbar dinamically basing on the active screen
        '''
        if current_screen == "new_user":
            self.right_action_items= []
            self.right_action_items = [["menu", lambda x: self.nav_drw.set_state("toggle")]]
            self.md_list.set_items(MDApp.get_running_app().privilege)
            pass
        elif current_screen == 'Logged_in_interface':
            self.right_action_items = []
            self.right_action_items = [["menu", lambda x: self.nav_drw.set_state("toggle")]]
            self.md_list.set_items(MDApp.get_running_app().privilege)
            pass
        else:
            self.right_action_items = []
            pass
        return
    pass


class New_user(Screen):
    pass


class Logged_in_interface(Screen):
    pass


class Log_in_screen(Screen):
    pass


class NavDrawerContent(MDList):
    list_items = {}

    def set_items(self, priviliges):
        '''

        :param priviliges: String parameter which define the number of element of nav drawer
        :return:
        The function each time the user log-in show only the nav drawer on priviliges bases
        '''
        #Define the navigation drawer list basing on user credential
        if priviliges == 'admin':
            items = {'database-export':'Export','database-remove':'Remove Record',
                     'account-plus':'Add User','account-remove':'Remove User','table-large-plus': "Add Table",
                     "table-remove": "Remove Table",'table-row-plus-after':'Add New Category',
                     'table-row-remove':'Remove Category','table-arrow-left':'Import Category Table',
                     'table-arrow-right':'Export Category Table','logout':'Logout'}
            pass
        elif priviliges == 'Quality':
            items = {'account-plus':'Add User','database-export': 'Export','database-remove':'Remove Record', 'table-row-plus-after': 'Add New Category',
                     'table-row-remove': 'Remove Category',
                     'table-arrow-right': 'Export Category Table','logout':'Logout'}
            pass
        else:
            items = {'logout':'Logout'}
            pass
        self.clear_widgets()
        self.list_items = items
        for i in self.list_items.keys():
            self.add_widget(List_item(text = self.list_items[i],icon = i))
            pass
        return

    def clicked(self,icon_clicked):
        '''

        :param icon_clicked: key of dict of icons
        :return:
        The function will all the proper method for screen managing
        '''

        print ("clicked icon {x}".format(x = icon_clicked))
        if icon_clicked == "logout": # Logout
            MDApp.get_running_app().set_screen("Log_in_Screen")
            pass
        elif icon_clicked == "table-arrow-right": # import Category
            pass
        elif icon_clicked == "table-arrow-left": # Export Category
            pass
        elif icon_clicked == "table-row-remove": # Remove Category
            pass
        elif icon_clicked == "table-row-plus-after": #Add New Category
            pass
        elif icon_clicked == "table-remove": #Remove Table
            pass
        elif icon_clicked == "table-large-plus": #Add Table
            pass
        elif icon_clicked == "account-remove": #Remove User
            pass
        elif icon_clicked == "account-plus": #Add User
            MDApp.get_running_app().set_screen("new_user")
            pass
        elif icon_clicked == "database-remove": #Remove Record
            pass
        elif icon_clicked == "database-export": #Export
            pass
        else:
            pass
        return
    pass


class List_item(OneLineIconListItem):
    icon = StringProperty()
    pass

if __name__ == '__main__':


    # create tabelle
    SQL_DB.create_table('Analisi')
    SQL_DB.create_table('Category')
    SQL_DB.create_table('Utenti')
    SQL_DB.create_table('Immagini')
    SQL_DB.create_table('Eventi')
    # Definizione colonne Utenti
    SQL_DB.add_col('Utenti', 'Nome', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    SQL_DB.add_col('Utenti', 'Cognome', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    SQL_DB.add_col('Utenti', 'Username', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    SQL_DB.add_col('Utenti', 'Password', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    SQL_DB.add_col('Utenti','Email','CHAR')
    SQL_DB.add_col('Utenti', 'Privilegi', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')

    # Definizione colonne Analisi
    SQL_DB.add_col('Analisi', 'Data','DATETIME')
    SQL_DB.add_col('Analisi', 'Utente', 'CHAR')
    SQL_DB.add_col('Analisi', 'Care', 'INT','NOT NULL DEFAULT \'00000000\'')
    SQL_DB.add_col('Analisi', 'Part_Number', 'CHAR')
    SQL_DB.add_col('Analisi', 'Serial_Number', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    SQL_DB.add_col('Analisi', 'Difetto', 'CHAR')
    SQL_DB.add_col('Analisi', 'Sub_Group', 'CHAR')
    SQL_DB.add_col('Analisi', 'Causa', 'CHAR')
    SQL_DB.add_col('Analisi', 'Responsabilità', 'CHAR')
    SQL_DB.add_col('Analisi', 'Semilavorato', 'CHAR')
    SQL_DB.add_col('Analisi', 'Note', 'LONGCHAR')
    SQL_DB.add_col('Analisi', 'Report', 'MEDIUMBLOB')

    # Definizione colonne Category
    SQL_DB.add_col('Category', 'Difetto', 'CHAR')
    SQL_DB.add_col('Category', 'Sub_Group', 'CHAR')
    SQL_DB.add_col('Category', 'Causa', 'CHAR')
    SQL_DB.add_col('Category', 'Responsabilità', 'CHAR')

    # Definizione colonne Immagini
    SQL_DB.add_col('Immagini', 'Care', 'INT', 'NOT NULL DEFAULT \'00000000\'')
    SQL_DB.add_col('Immagini', 'Serial_Number', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    SQL_DB.add_col('Immagini', 'Cosmetica', 'MEDIUMBLOB')
    SQL_DB.add_col('Immagini', 'Analisi', 'MEDIUMBLOB')

    # Definizione colonne Eventi
    SQL_DB.add_col('Eventi', 'Care', 'INT', 'NOT NULL DEFAULT \'00000000\'')
    SQL_DB.add_col('Eventi', 'Serial_Number', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    SQL_DB.add_col('Eventi', 'Log_Eventi', 'MEDIUMBLOB')
    SQL_DB.add_col('Eventi', 'Statistiche', 'MEDIUMBLOB')
    # Inserimento utente Base
    record_base = {'Nome':'Andrea','Cognome':'Naldini','Username':'Naldadoc','Email':'andrea.naldini@it.abb.com',
                   'Password':'Root','Privilegi':'admin'}
    record_quality_test ={'Nome':'Quality','Cognome':'Process','Username':'Quality','Password':'Quality','Email':'Quality.test@it.abb.com','Privilegi':'Quality'}
    record_repair_test = {'Nome':'Rework','Cognome':'Repair','Username':'Rework','Password':'Production','Email':'Quality.test@it.abb.com','Privilegi':'Production'}
    l = SQL_DB.search_loc('Utenti', 'Nome', 'Admin')
    if not l:
        SQL_DB.insert_record('Utenti', record_base)
        SQL_DB.insert_record('Utenti', record_quality_test)
        SQL_DB.insert_record('Utenti', record_repair_test)
        pass
    records = SQL_DB.show_records('Utenti')
    print(records)
    SQL_DatabaseApp().run()
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
