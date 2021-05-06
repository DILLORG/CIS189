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
from .exceptions import NotEnoughGoldError

ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
DATA_PATH = os.path.join(os.getcwd(), 'data')
MAIN_GLADE_FILE = os.path.join(ASSETS_PATH, 'main.glade')
PROFILE = os.path.join(DATA_PATH, 'app.data')
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

        """
        These Listore objects make updating and inserting data into the gui
        easy but they get in the way of my base class. # QUESTION: would I
        have been better of giving up on Gtk altogether and going with an HTML
        parsing library.
        """
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

    def create_tree_view_headings(self, treeView, headings):
        """
        Create treeView headings.
        :params treeView object, list of heading names.
        :returns none.
        """
        for index, title in enumerate(headings):
            cell = Gtk.CellRendererText()
            heading = Gtk.TreeViewColumn(title, cell, text=index)
            treeView.append_column(heading)

    def load_profile(self):
        """
        Load the player's profile from the data folder.
        :params none.
        :returns none.
        """
        try:
            with open(PROFILE, 'rb') as file:
                self.__player = load(file)

                for skill in self.__player.skills:
                    self.__skillStore.append(skill)

                for quest in self.__player.quests:
                    self.__questStore.append(quest)

                for item in self.__player.shop:
                    self.__shopStore.append(item)

                self.update_profile()

        except (OSError, IOError, EOFError):
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
        """
        Show Quest dialog.
        :params none.
        :returns none.
        """
        self.__questDialog.show()

    def on_questDialog_response(self, widget):
        """
        Process questForm
        :params none.
        :returns none.
        """
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

    def on_quest_selected(self, treeView, row, column):
        """
        Quest completed add gold and skill points.
        :params treeView object, row selected, column.
        """
        model = treeView.get_model()
        name = model[row][0]
        reward = model[row][1]
        skill = model[row][2]
        del model[row]

        self.__player.add_gold(reward)
        self.__player.level += 1
        self.update_profile()

        # Search for relevant skill
        for row in self.__skillStore:
            if row[0] == skill:
                row[1] += 1

        self.write_to_message_area(SUCCESS_COLOR, f"Completed Quest {name}")

    def add_skill(self, widget):

        self.__skillDialog.show()

    def on_skillDialog_response(self, widget):
        """
        Process skill form.
        :params calling widget.
        :returns none.
        """

        # Button that was clicked.
        response = Gtk.Buildable.get_name(widget)

        if response == 'submitSkill':
            name = self.__skillNameTb.get_text()
            skillExist = False

            # Check if the player if the player already has this skill.
            for row in self.__skillStore:
                if row[0] == name:
                    skillExist = True

            if not skillExist:
                self.__skillStore.append([name, 0])
                self.write_to_message_area(SUCCESS_COLOR, f"Added '{name}' to skills")

            else:
                self.write_to_message_area(FAIL_COLOR, f"Failed to add  skill '{name}' it is already one of your skills")

        self.__skillNameTb.set_text('')
        self.__skillDialog.hide()

    def add_shop_item(self, widget):
        """
        Display shop dialog.
        :params none.
        :returns none.
        """
        self.__shopDialog.show()

    def on_shopDialog_response(self, widget):
        """
        Process shop form and add item.
        :params calling widget.
        """
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

    def on_item_selected(self, treeView, row, column):
        model = treeView.get_model()
        name = model[row][0]
        price = model[row][1]

        try:
            self.__player.remove_gold(price)
            del model[row]
            self.write_to_message_area(SUCCESS_COLOR, f"You bought a '{name}' enjoy your reward")
            self.update_profile()

        except NotEnoughGoldError:
            self.write_to_message_area(FAIL_COLOR, f"'{name}' is to expensive")

    def update_profile(self):
        """
        Update the profile page so that it shows the current data members of
        the player object.
        :params none.
        :returns none.
        """
        self.__nameLbl.set_text(self.__player.name)
        self.__levelLbl.set_text(str(self.__player.level))
        self.__goldLbl.set_text(str(self.__player.gold))
        self.__typeLbl.set_text(str(self.__player.type))

    def save_profile(self):
        """
        Use Pickle to save the player's status.
        Gtk.Listore objects are incompatiable so convert to list.
        # TODO: See if there is a more efficent way of doing this.
        """
        skills = []
        quest = []
        shop = []

        for row in self.__skillStore:
            name = row[0]
            level = row[1]
            skills.append([name, level])

        for row in self.__shopStore:
            name = row[0]
            price = row[1]
            shop.append([name, price])

        for row in self.__questStore:
            name = row[0]
            gold = row[1]
            skill = row[2]
            date = row[3]
            quest.append([name, gold, skill, date])

        self.__player.skills = skills
        self.__player.shop = shop

        with open(PROFILE, 'wb') as file:
            dump(self.__player, file)

    def write_to_message_area(self, color, message):
        """
        Write any error or success message to the Message Area
        :params color background color of message,
        message text to display
        :returns none.
        """
        markup = f"<span background={color}>{message}</span>"
        self.__messageLabel.set_markup(markup)
        self.__messageArea.popup()
        self.message_time_out()

    @threaded
    def message_time_out(self):
        """
        Hide the message area after a time.
        :params none.
        :returns none.
        """
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
        """
        Run the main loop.
        :parms none.
        :returns none.
        """
        Gtk.main()
