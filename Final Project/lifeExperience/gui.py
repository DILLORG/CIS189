import gi
import os
import sys
import threading
import time
from datetime import datetime
from pickle import dump, load
from gi.repository import Gtk, GLib
from .player import Player
from re import match

ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
MAIN_GLADE_FILE = os.path.join(ASSETS_PATH, 'main.glade')
PROFILE = os.path.join(ASSETS_PATH, 'player.profile')
SUCCESS_COLOR = '\'#25f764\''
FAIL_COLOR = '\'#f73416\''
POSITIVE_INTERGER = '[1-9][0-9]*'


def threaded(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs).start()
    return wrapper


class MainWindow(Gtk.Window):
    def __init__(self):
        """
        Main app app window.
        :params player player's data.
        :returns Main window.
        """

        self.__player = Player()

        __builder = Gtk.Builder()
        __builder.add_from_file(MAIN_GLADE_FILE)
        __builder.connect_signals(self)

        # Model and views.
        self.__skillStore = Gtk.ListStore(str, int)
        self.__skillView = __builder.get_object('skillsList')
        self.__skillView.set_model(self.__skillStore)
        self.create_tree_view_headings(self.__skillView, ['Skill Name',
                                                          'Level'])
        self.__questStore = Gtk.ListStore(str, int, str, str)
        self.__questView = __builder.get_object('questList')
        self.__questView.set_model(self.__questStore)
        self.create_tree_view_headings(self.__questView, ['Quest Name',
                                                          'Gold Reward',
                                                          'Skill',
                                                          'Date Due'])
        self.__shopStore = Gtk.ListStore(str, int)
        self.__shopView = __builder.get_object('shopList')
        self.__shopView.set_model(self.__shopStore)
        self.create_tree_view_headings(self.__shopView, ['Item Name', 'Price'])

        # Profile Page
        self.__nameLbl = __builder.get_object('nameLbl')
        self.__levelLbl = __builder.get_object('levelLbl')
        self.__goldLbl = __builder.get_object('goldLbl')
        self.__typeLbl = __builder.get_object('typeLbl')
        self.__window = __builder.get_object('mainWindow')

        # Edit Dialog
        self.__editPlayer = __builder.get_object('editDialog')
        self.__nameTb = __builder.get_object('nameTb')
        self.__typeTb = __builder.get_object('typeTb')

        # Quest Dialog
        self.__questDialog = __builder.get_object('questDialog')
        self.__questNameTb = __builder.get_object('questNameTb')
        self.__goldTb = __builder.get_object('goldTb')
        self.__dueDateTb = __builder.get_object('dueDateTb')
        self.__skillCb = __builder.get_object('skillCb')
        self.__skillCb.set_model(self.__skillStore)

        # Skill Dialog
        self.__skillDialog = __builder.get_object('skillDialog')
        self.__skillNameTb = __builder.get_object('skillNameTb')

        # Shop Dialog
        self.__shopDialog = __builder.get_object('shopDialog')
        self.__itemTb = __builder.get_object('itemTb')
        self.__priceTb = __builder.get_object('priceTb')

        # Message Area.
        self.__messageArea = __builder.get_object('messageArea')
        self.__messageLabel = __builder.get_object("messageLabel")
        self.__window.show_all()

        self.load_profile()
        self.update_profile()

    def create_tree_view_headings(self, treeView, headings):
        for index, title in enumerate(headings):
            cell = Gtk.CellRendererText()
            heading = Gtk.TreeViewColumn(title, cell, text=index)
            treeView.append_column(heading)

    def load_profile(self):
        try:
            with open(PROFILE, 'rb') as file:
                self.__player = load(file)

        except (OSError, IOError):
            self.save_profile()

    def edit_player(self, widget):
        self.__editPlayer.show()

    def on_editDialog_response(self, widget):
        response = Gtk.Buildable.get_name(widget)
        if response == 'submitEdit':
            self.__player.name = self.__nameTb.get_text()
            self.__player.type = self.__typeTb.get_text()
            self.update_profile()
            self.write_to_message_area(SUCCESS_COLOR, "Updated player profile")

        self.__nameTb.set_text('')
        self.__typeTb.set_text('')
        self.__editPlayer.hide()

    def add_quest(self, widget):
        self.__questDialog.show()

    def on_questDialog_response(self, widget):
        response = Gtk.Buildable.get_name(widget)
        if response == 'submitQuest':

            gold = self.__goldTb.get_text()

            if(match(POSITIVE_INTERGER, gold)):
                dueDate = self.__dueDateTb.get_text()

                try:
                    dueDate = datetime.strptime(dueDate, '%m-%d-%Y %H:%M')
                    questName = self.__questNameTb.get_text()
                    skill = self.__skillCb.get_active_text()
                    self.__questStore.append([questName, int(gold), skill,
                                              str(dueDate)])

                    self.write_to_message_area(SUCCESS_COLOR, f"The Quest {questName} has been added")

                except ValueError:
                    self.write_to_message_area(FAIL_COLOR, "Improper Date please input as mm-dd-yyyy hh:mm format")

            else:
                self.write_to_message_area(FAIL_COLOR, f"{gold} is an invalid value for Gold")

        self.__questNameTb.set_text('')
        self.__dueDateTb.set_text('')
        self.__questDialog.hide()

    def add_skill(self, widget):
        self.__skillDialog.show()

    def on_skillDialog_response(self, widget):
        response = Gtk.Buildable.get_name(widget)
        if response == 'submitSkill':
            name = self.__skillNameTb.get_text()
            self.__skillStore.append([name, 0])
            self.write_to_message_area(SUCCESS_COLOR, f"Added {name} to skills")

        self.__skillNameTb.set_text('')
        self.__skillDialog.hide()

    def add_shop_item(self, widget):
        self.__shopDialog.show()

    def on_shopDialog_response(self, widget):
        response = Gtk.Buildable.get_name(widget)
        if response == 'submitItem':
            price = self.__priceTb.get_text()
            if match(POSITIVE_INTERGER, price):
                name = self.__itemTb.get_text()
                self.__shopStore.append([name, int(price)])
                self.write_to_message_area(SUCCESS_COLOR, f"Added {name} to shop.")

        self.__priceTb.set_text('')
        self.__itemTb.set_text('')

        self.__shopDialog.hide()

    def update_profile(self):
        self.__nameLbl.set_text(self.__player.name)
        self.__levelLbl.set_text(str(self.__player.get_skill_level('Player')))
        self.__goldLbl.set_text(str(self.__player.gold))
        self.__typeLbl.set_text(str(self.__player.type))

    def save_profile(self):
        with open(PROFILE, 'wb') as file:
            dump(self.__player, file)

    def write_to_message_area(self, color, message):
        markup = f"<span background={color}>{message}</span>"
        self.__messageLabel.set_markup(markup)
        self.__messageArea.popup()
        self.message_time_out()

    @threaded
    def message_time_out(self):
        time.sleep(3)
        GLib.idle_add(self.__messageArea.popdown)

    def close_app(self, widget, event):
        """
        Quit the main loop of the program.
        :params widget, event
        :returns none
        """
        Gtk.main_quit()
        self.save_profile()
        sys.exit()

    def run_app(self):
        Gtk.main()
