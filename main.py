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

FALAB_DB = sqlite_creator.DB_sqlite(PATH,'FALAB_db.db',separatore)



class FALAB_DatabaseApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'BlueGray'
        self.theme_cls.theme_style = 'Light'
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
        print(username ,' + ', password)
        return

    def add_user(self):
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
            self.right_action_items = [["arrow-left-thick",lambda x: MDApp.get_running_app().set_screen("Log_in_Screen")]]
            pass
        elif current_screen == 'Logged_in_interface':
            self.right_action_items = []
            self.left_action_items = []
            self.right_action_items = [["arrow-left-thick", lambda x: MDApp.get_running_app().set_screen("Log_in_Screen")],
                ["menu", lambda x: self.nav_drw.set_state("toggle")]]
            self.md_list.set_items("Admin")
            pass
        else:
            self.right_action_items = []
            self.left_action_items = []
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

    def set_items(self,priviliges):
        '''

        :param priviliges: String parameter which define the number of element of nav drawer
        :return:
        The function each time the user log-in show only the nav drawer on priviliges bases
        '''
        #Define the navigation drawer list basing on user credential
        if priviliges == 'Admin':
            items = {'database-export':'Export','database-remove':'Remove Record',
                     'account-plus':'Add User','account-remove':'Remove User','table-large-plus': "Add Table",
                     "table-remove": "Remove Table",'table-row-plus-after':'Add New Category',
                     'table-row-remove':'Remove Category','table-arrow-left':'Import Category Table',
                     'table-arrow-right':'Export Category Table','logout':'Logout'}
            pass
        elif priviliges == 'Quality':
            items = {'database-export': 'Export','database-remove':'Remove Record', 'table-row-plus-after': 'Add New Category',
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
        return
    pass


class List_item(OneLineIconListItem):
    icon = StringProperty()
    pass



if __name__ == '__main__':
    # create new db

    # create tabelle
    FALAB_DB.create_table('Analisi')
    FALAB_DB.create_table('Category')
    FALAB_DB.create_table('Utenti')
    FALAB_DB.create_table('Immagini')
    FALAB_DB.create_table('Eventi')
    # Definizione colonne Utenti
    FALAB_DB.add_col('Utenti', 'Nome', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Cognome', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Username', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Password', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')
    FALAB_DB.add_col('Utenti', 'Privilegi', 'CHAR', 'NOT NULL DEFAULT \'Missing\'')

    # Definizione colonne Analisi
    FALAB_DB.add_col('Analisi', 'Data','DATETIME')
    FALAB_DB.add_col('Analisi', 'Utente', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Care', 'INT','NOT NULL DEFAULT \'00000000\'')
    FALAB_DB.add_col('Analisi', 'Part_Number', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Serial_Number', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    FALAB_DB.add_col('Analisi', 'Difetto', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Sub_Group', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Causa', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Responsabilità', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Semilavorato', 'CHAR')
    FALAB_DB.add_col('Analisi', 'Note', 'LONGCHAR')
    FALAB_DB.add_col('Analisi', 'Report', 'MEDIUMBLOB')

    # Definizione colonne Category
    FALAB_DB.add_col('Category', 'Difetto', 'CHAR')
    FALAB_DB.add_col('Category', 'Sub_Group', 'CHAR')
    FALAB_DB.add_col('Category', 'Causa', 'CHAR')
    FALAB_DB.add_col('Category', 'Responsabilità', 'CHAR')

    # Definizione colonne Immagini
    FALAB_DB.add_col('Immagini', 'Care', 'INT', 'NOT NULL DEFAULT \'00000000\'')
    FALAB_DB.add_col('Immagini', 'Serial_Number', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    FALAB_DB.add_col('Immagini', 'Cosmetica', 'MEDIUMBLOB')
    FALAB_DB.add_col('Immagini', 'Analisi', 'MEDIUMBLOB')

    # Definizione colonne Eventi
    FALAB_DB.add_col('Eventi', 'Care', 'INT', 'NOT NULL DEFAULT \'00000000\'')
    FALAB_DB.add_col('Eventi', 'Serial_Number', 'INT', 'NOT NULL DEFAULT \'0000000000\'')
    FALAB_DB.add_col('Eventi', 'Log_Eventi', 'MEDIUMBLOB')
    FALAB_DB.add_col('Eventi', 'Statistiche', 'MEDIUMBLOB')
    # Inserimento utente Base
    record_base = {'Nome':'Admin','Cognome':'root','Username':'admin','Password':'Root','Privilegi':'admin'}
    record_quality_test ={'Nome':'Quality','Cognome':'Process','Username':'Quality','Password':'Quality','Privilegi':'Quality'}
    record_repair_test = {'Nome':'Rework','Cognome':'Repair','Username':'Rework','Password':'Production','Privilegi':'Production'}
    l = FALAB_DB.search_loc('Utenti', 'Nome', 'Admin')
    if not l:
        FALAB_DB.insert_record('Utenti', record_base)
        FALAB_DB.insert_record('Utenti', record_quality_test)
        FALAB_DB.insert_record('Utenti', record_repair_test)
        pass
    records = FALAB_DB.show_records('Utenti')
    print(records)
    FALAB_DatabaseApp().run()
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
