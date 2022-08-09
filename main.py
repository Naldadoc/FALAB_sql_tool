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
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


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
        self.dialog = User_dialog(title = 'User already registered',content_cls = Box_Contenent())
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
        #check the error status of labels
        err = bool()
        user_dict = {'Nome': nome,'Cognome':cognome,'Username':username,'Password':password,'Email':email, 'Privilegi':privilegi}
        for i in user_dict.keys():
            if user_dict[i] == '':
                err = False
                break
                pass
            else:
                err = True
                pass
            pass

        if err:
            l = SQL_DB.search_loc('Utenti',"Username",username)
            if l:
                self.dialog.title = 'User already registered'
                self.dialog.open()
                pass
            else:
                SQL_DB.insert_record('Utenti',user_dict)
                self.dialog.title = 'User Added'
                self.dialog.open()
                pass
            pass
        else:
            self.dialog.title = 'Missing Elements'
            self.dialog.open()
            pass
        return

    def set_screen(self, next_scr):

        self.prev_screen = self.root.ids.root_screen.current
        self.root.ids.root_screen.current = next_scr
        print("old:{x} and new: {y}".format(x = self.prev_screen,y=next_scr))
        self.root.ids.nav_drw.set_state("toggle")
        return

    def mng_dialog(self,title):
        if title == 'User Added':

            self.root.ids.root_screen.current= 'Logged_in_interface'
            self.dialog.dismiss(force=True)
            pass
        elif title == 'User already registered':

            self.dialog.dismiss(force=True)

            pass
        elif title == 'Missing Elements':
            self.dialog.dismiss(force=True)
        else:
            pass
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
            self.root_screen.get_screen('new_user').clear_fields()
            self.nav_drw.set_state("toggle")
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

    def round_active(self):
        '''
        The function scan the check box buttons and return the selected string
        :return:
        '''
        if self.ids.quality_check_btn.active:
            credential = 'Quality'
            pass
        elif self.ids.production_check_btn.active:
            credential = 'Production'
            pass
        else:
            credential = ''
            pass
        return credential

    def clear_fields(self):
        self.ids.Nome_input.text = ''
        self.ids.Cognome_input.text = ''
        self.ids.Username_input.text = ''
        self.ids.e_mail.text = ''
        self.ids.New_password_input.text = ''
        return
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

class Box_Contenent(BoxLayout):
    pass

class User_dialog(MDDialog):
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
    l = SQL_DB.search_loc('Utenti', 'Nome', 'Andrea')
    if not l:
        SQL_DB.insert_record('Utenti', record_base)
        pass
    records = SQL_DB.show_records('Utenti')
    for i in records:
        print(i)
        pass
    SQL_DatabaseApp().run()
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
