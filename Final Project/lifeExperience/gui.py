import gi
import os
import sys
from pickle import dump, load
from gi.repository import Gtk
from .player import Player

ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
GLADE_FILE = os.path.join(ASSETS_PATH, 'main.glade')
PROFILE = os.path.join(ASSETS_PATH, 'player.profile')


class MainWindow:
    def __init__(self):
        """
        Main app app window.
        :params player player's data.
        :returns Main window.
        """
        self.__player = Player()

        __builder = Gtk.Builder()
        __builder.add_from_file(GLADE_FILE)
        __builder.connect_signals(self)
        self.load_profile()
        self.__nameLbl = __builder.get_object('nameLbl')
        self.__leveLbl = __builder.get_object('leveLbl')
        self.__xpLbl = __builder.get_object('xpLbl')
        self.__classLbl = __builder.get_object('classLbl')
        self.__mainWindow = __builder.get_object('mainWindow')
        self.__profilePic = __builder.get_object('profilePic')
        self.__timeLbl = __builder.get_object('timeLbl')
        self.__mainWindow.show_all()

    def load_profile(self):
        try:
            with open(PROFILE, 'rb') as file:
                self.__player = load(file)

        except (OSError, IOError):
            self.save_profile()

    def edit_player(self, event):
        print('Clicked')

    def save_profile(self):
        with open(PROFILE, 'wb') as file:
            dump(self.__player, file)

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
