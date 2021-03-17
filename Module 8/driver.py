import tkinter
from taxes import *


def on_submit_click():
    income = incomeVar.get()
    result = calculate_single_tax(income)
    statusLbl.config(text=result)


window = tkinter.Tk()

window.title('Calculate Single Tax')

statusLbl = tkinter.Label(window, text="")
incomeLbl = tkinter.Label(window, text="Enter Income:")
incomeVar = tkinter.IntVar()
incomeEntry = tkinter.Entry(window, textvariable=incomeVar, width=20,
                            bg='white')

button = tkinter.Button(window, text='Submit', width=25,
                        command=on_submit_click)


incomeLbl.grid(row=1, column=0)
incomeEntry.grid(row=1, column=1)
button.grid(row=2, column=0)
statusLbl.grid(row=3, column=0)

window.mainloop()
