import gi
import os
import sys
import threading
import time
from .numberGuesser import NumberGuesser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib


def threaded(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs).start()
    return wrapper


class NumberGuesserGui:
    def __init__(self):
        """
        Create the Gui for our number guessing game.
        """

        __ASSETS_PATH = os.path.join(os.path.join(os.getcwd(), 'assets'),
                                     'main.glade')
        self.__AMOUNT = 9
        self.__MIN = 1
        self.__MAX = 100

        __builder = Gtk.Builder()
        __builder.add_from_file(__ASSETS_PATH)
        __builder.connect_signals(self)

        self.__messageArea = __builder.get_object("messageArea")
        self.__messageLabel = __builder.get_object("messageLabel")
        self.__messageLabel.set_markup("<span background='#00ff00'>Winner!</span>")

        self.__gameBoard = __builder.get_object("gameBoard")
        self.__window = __builder.get_object("mainWindow")

        self.__numberGuesser = NumberGuesser(self.__MIN, self.__MAX, self.__AMOUNT)

        self.generate_labels()
        self.__window.show_all()

    def new_game(self, widget):

        self.__numberGuesser = NumberGuesser(self.__MIN, self.__MAX, self.__AMOUNT)
        self.generate_labels()

    def generate_labels(self):
        labels = iter(self.__numberGuesser.get_possibles())
        for button in self.__gameBoard.get_children():
            button.set_sensitive(True)
            button.set_label(str(next(labels)))

    def guess_number(self, widget):
        self.__numberGuesser.add_guess(widget.get_label())
        widget.set_sensitive(False)
        self.check_winner()

    @threaded
    def message_time_out(self):
        time.sleep(3)
        GLib.idle_add(self.__messageArea.popdown)

    def check_winner(self):
        """
        Check if the user guessed correctly. If they did turn off
        input to the game board and display the winning message.
        :params none.
        :returns none.
        """
        if self.__numberGuesser.is_winner():

            # Disable all buttons
            for button in self.__gameBoard.get_children():
                button.set_sensitive(False)

            # Display message
            self.__messageArea.popup()
            self.message_time_out()

    def close_app(self, widget, event):
        """
        Quit the main loop of the app.
        :params none.
        :returns none.
        """
        Gtk.main_quit()
        return

    def run_app(self):
        """
        Run the app.
        :params none.
        returns none.
        """
        Gtk.main()
