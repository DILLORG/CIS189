import gi
import os
from gi.repository import Gtk


class MainWindow:
    def __init__(self, player):
        """
        Main app app window.
        :params player player's data.
        :returns Main window.
        """
        self.__player = player

        __ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
        __GLADE_FILE = os.path.join(__ASSETS_PATH, 'main.glade')
        __builder = Gtk.Builder()
        __builder.add_from_file(__GLADE_FILE)
        __builder.connect_signals(self)

        self.__mainWindow = __builder.get_object('mainWindow')
        self.__mainWindow.show_all()

    def close_app(self, widget, event):
        """
        Quit the main loop of the program.
        :params widget, event
        :returns none
        """
        Gtk.main_quit()

    def run_app(self):
        Gtk.main()
