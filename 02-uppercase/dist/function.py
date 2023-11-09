from tkinter import *
from tkinter import messagebox

from notify import *

def on_focus_in(entry):
    if entry.cget('state') == DISABLED:
        entry.configure(state= NORMAL)
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state=DISABLED)

def focus_io(entry, s):
    entry.insert(0, s)
    entry.configure(state=DISABLED)
    input_focus_in = entry.bind('<Button-1>', lambda x: on_focus_in(entry))
    input_focus_out = entry.bind('<FocusOut>', lambda x: on_focus_out(entry, s))

def convert(entryOutput, stringLower):
    if stringLower == '':
        messagebox.showwarning(NAME_WARNING_BOX, MESSAGE_WARNING_BOX)
        return
    on_focus_in(entryOutput)
    entryOutput.delete(0,'end')
    entryOutput.insert(0, stringLower.upper())

def clear(entryOutput, entryInput, stringUpper, stringOutput):
    msgBox = messagebox.askquestion(NAME_CONFIRM_BOX, MASSAGE_CONFIRM_BOX, icon = 'warning')
    if msgBox == 'yes':
        entryOutput.delete(0,'end')
        entryInput.delete(0, 'end')
        focus_io(entryOutput, stringOutput)