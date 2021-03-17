"""
Program: driver
Author: Dylan Kennedy
Last date modified: 03/17/2021

Displays window with Radiobutton allowing the user to select their favorite
meal. Once selected the label is updated with their choice.
"""
import tkinter as tk
from tkinter.font import Font


class Window(tk.Tk):

    def __init__(self):
        """
        Intialize window object set the geometry and window title and calls
        load_widgets which constructs all the windows widgets.
        :params none
        :returns Window object.
        """
        super().__init__()
        self.geometry('250x250')
        self.title('Favorite Food')
        self.font = Font(family='TkFixedFont', size=12)
        self.resizable(0, 0)
        self.load_widgets()

    def load_widgets(self):
        """
        Construct all Widgets for window.
        :params self.
        :returns constructed widgets binded to the Applications gui.
        """
        # Used as labels and values for Radiobutton.
        meals = ['Break Fast', 'Second Break Fast', 'Lunch', 'Dinner']

        # Used to hold a the coresponding value for the Radiobutton.
        choice = tk.StringVar()

        """
        For the length of meals set the Radiobutton row to the to the current
        value of x. Set the text next to the radio button to the meal type.
        Set the variable to choice. Set the command to a on_choice function.
        When A Radiobutton is selected the coresponding value is
        passed to the on_choice function. I choose over checkbuttons because
        logically a person can only have one favorite meal.
        """
        for x in range(len(meals)):
            # Programatically decalare the Radiobuttons.
            rb = tk.Radiobutton(self, text=meals[x], variable=choice,
                                value=meals[x], font=self.font,
                                command=lambda: self.on_choice(choice.get()))
            # Set the row.
            rb.grid(row=x)

        # Outputlabel
        self.faveMealLbl = tk.Label(self, text="Waiting", font=self.font)
        self.faveMealLbl.grid(row=5)

        # Close program.
        self.exitBtn = tk.Button(self, text='Exit', font=self.font,
                                 command=self.on_exit_click)
        self.exitBtn.grid(row=6)

    def on_exit_click(self):
        """
        Closes program when binded button is clicked.
        :params none
        :returns none
        """
        exit()

    def on_choice(self, value):
        """
        Shows users favorite meal on the status label.
        :params none
        :returns none
        """
        self.faveMealLbl.config(text=f"You choose {value}")


if __name__ == '__main__':
    window = Window()
    window.mainloop()
