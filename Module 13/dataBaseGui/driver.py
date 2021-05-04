from dataBase.appDataBase import AppDataBase
import gi
import os
import sys
from gi.repository import Gtk
from gi.repository import GLib


class DataBaseGUI:
    def __init__(self):
        self.__appDataBase = AppDataBase(':memory:')

        if self.__appDataBase:
            __ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
            __GLADE_FILE = os.path.join(__ASSETS_PATH, 'main.glade')

            self.__builder = Gtk.Builder()
            self.__builder.add_from_file(__GLADE_FILE)
            self.__builder.connect_signals(self)

            self.__personLB =  self.__builder.get_object('personLB')
            self.__studentLB = self.__builder.get_object('studentLB')

            self.__mainWindow = self.__builder.get_object('mainWindow')
            self.__addPersonWindow = self.__builder.get_object('addPersonDialog')
            self.__addStudentWindow = self.__builder.get_object('addStudentDialog')
            self.__firstNameEntryPerson = self.__builder.get_object('firstNameEntryPerson')
            self.__lastNameEntryPerson = self.__builder.get_object('lastNameEntryPerson')
            self.__firstNameEntryStudent = self.__builder.get_object('firstNameEntryStudent')
            self.__lastNameEntryStudent = self.__builder.get_object('lastNameEntryStudent')
            self.__majorEntryStudent = self.__builder.get_object('majorEntryStudent')
            self.__startDateEntryStudent = self.__builder.get_object('startDateEntryStudent')

            self.__mainWindow.show_all()

        else:
            raise ValueError("Failed to load dabase")

    def on_createPersonBtn_clicked(self, widget):
        self.__addPersonWindow.show()

    def on_createStudentBtn_clicked(self, widget):
        self.__addStudentWindow.show()

    def on_addPersonDialog_response(self, widget):
        response = Gtk.Buildable.get_name(widget)

        if response == 'submitPerson':
            firstName = self.__firstNameEntryPerson.get_text()
            lastName = self.__lastNameEntryPerson.get_text()
            person = self.__appDataBase.create_person(firstName, lastName)

            self.__firstNameEntryPerson.set_text('')
            self.__lastNameEntryPerson.set_text('')

            """Can't find a good way to update the model and remove duplicates
            My code alreay queries corectly queries the dataBase the problem is
            this takes more time to implement in GTK. I imaging it is also
            difficult in tkinter. It stores items in the database."""
            self.__personLB.add(Gtk.Label(label=str(person)))
            self.__personLB.show_all()

        self.__addPersonWindow.hide()

    def on_addStudentDialog_response(self, widget):
        """
        Get the name of the calling widget if the submit button was clicked
        get the text from the entries and store in the database.
        if the response was not cancel then hide the window.
        :params calling widget
        :returns none
        """
        resposne = Gtk.Buildable.get_name(widget)

        # User seleceted submit.
        if resposne == 'submitStudent':

            firstName = self.__firstNameEntryStudent.get_text()
            lastName = self.__lastNameEntryStudent.get_text()
            major = self.__majorEntryStudent.get_text()
            startDate = self.__startDateEntryStudent.get_text()
            self.__firstNameEntryStudent.set_text('')
            self.__lastNameEntryStudent.set_text('')
            self.__majorEntryStudent.set_text('')
            self.__startDateEntryStudent.set_text('')

            """Can't find a good way to update the model and remove duplicates
            My code alreay queries corectly queries the dataBase the problem is
            this takes more time to implement in GTK. I imaging it is also
            difficult in tkinter. It stores items in the database."""
            student = self.__appDataBase.create_student(firstName, lastName, major, startDate)
            self.__studentLB.add(Gtk.Label(label=str(student)))
            self.__studentLB.show_all()

        # Hide window.
        self.__addStudentWindow.hide()

    def close_app(self, widget, event):
        """
        Quit the main loop of the program and exit.
        :params calling widget, event.
        :returns none.
        """
        Gtk.main_quit()
        sys.exit()

    def run_app(self):
        """
        Start the main loop with the progra.
        :params none.
        :returns none.
        """
        Gtk.main()


if __name__ == '__main__':
    app = DataBaseGUI()
    app.run_app()
