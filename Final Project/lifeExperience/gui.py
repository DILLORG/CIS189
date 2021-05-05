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

        # Model and views.
        self.__skillStore = Gtk.ListStore(str, int)
        self.__skillView = __builder.get_object('skillsList')
        self.__skillView.set_model(self.__skillStore)
        self.create_tree_view_headings(self.__skillView, ['Skill Name',
                                                          'Level'])
        self.__questStore = Gtk.ListStore(str, int, str, int)
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
        self.__xpTb = __builder.get_object('xpTb')
        self.__dueDateTb = __builder.get_object('dueDateTb')
        self.__questStore = Gtk.ListStore(str, int, str, int)
        self.__skillCb = __builder.get_object('skillCb')
        self.__skillCb.set_model(self.__skillStore)

        # Skill Dialog
        self.__skillDialog = __builder.get_object('skillDialog')
        self.__skillNameTb = __builder.get_object('skillNameTb')

        # Shop Dialog
        self.__shopDialog = __builder.get_object('shopDialog')
        self.__itemTb = __builder.get_object('itemTb')
        self.__priceTb = __builder.get_object('priceTb')

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
        if response == "submitEdit":
            self.__player.name = self.__nameTb.get_text()
            self.__player.type = self.__typeTb.get_text()
            self.update_profile()

            self.__nameTb.set_text('')
            self.__typeTb.set_text('')
        self.__editPlayer.hide()

    def add_quest(self, widget):
        self.__questDialog.show()

    def on_questDialog_response(self, widget):
        self.__questDialog.hide()

    def add_skill(self, widget):
        self.__skillDialog.show()

    def on_skillDialog_response(self, widget):
        self.__skillDialog.hide()

    def add_shop_item(self, widget):
        self.__shopDialog.show()

    def on_shopDialog_response(self, widget):
        self.__shopDialog.hide()

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
