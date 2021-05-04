import gi
import os
import sys
from pickle import dump, load
from gi.repository import Gtk
from .player import Player
from re import match

ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
MAIN_GLADE_FILE = os.path.join(ASSETS_PATH, 'main.glade')
PROFILE = os.path.join(ASSETS_PATH, 'player.profile')


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

        self.__nameLbl = __builder.get_object('nameLbl')
        self.__levelLbl = __builder.get_object('levelLbl')
        self.__goldLbl = __builder.get_object('goldLbl')
        self.__typeLbl = __builder.get_object('typeLbl')
        self.__window = __builder.get_object('mainWindow')
        self.__editPlayer = __builder.get_object('editDialog')
        self.__nameTb = __builder.get_object('nameTb')
        self.__typeTb = __builder.get_object('typeTb')
        self.__window.show_all()

        self.load_profile()
        self.update_profile()

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
        if response == "submitEdit":
            self.__player.name = self.__nameTb.get_text()
            self.__player.type = self.__typeTb.get_text()
            self.update_profile()

            self.__nameTb.set_text('')
            self.__typeTb.set_text('')
        self.__editPlayer.hide()

    def update_profile(self):
        self.__nameLbl.set_text(self.__player.name)
        self.__levelLbl.set_text(str(self.__player.get_skill_level('Player')))
        self.__goldLbl.set_text(str(self.__player.gold))
        self.__typeLbl.set_text(str(self.__player.type))

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
