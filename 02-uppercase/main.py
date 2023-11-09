from tkinter import *
#from tkmacosx import Button
import os

from define import *
from app import App
from function import *
from class_widget import MyFrame, MyLabel, MyEntry, MyButton

# Init
root = Tk()
# Set Window
app = App(root)

# Set Frame
frameLeft = MyFrame(root)
frameLeft.grid(column = 0)
frameRight = MyFrame(root)
frameRight.grid(column = 1)

# Input
labelLeft = MyLabel(frameLeft, text = 'Input')
entryInput = MyEntry(frameLeft)
entryInput.focus()
focus_io(entryInput, stringInput)
buttonConvert = MyButton(frameLeft, text = 'Convert', bg = '#82E0AA', command= lambda: convert(entryOutput, entryInput.get()))

# Output
labelRight = MyLabel(frameRight, text = 'Output')
entryOutput = MyEntry(frameRight)
focus_io(entryOutput, stringOutput)
buttonClear = MyButton(frameRight, text = 'Clear',bg = '#EC7063', command= lambda: clear(entryOutput, entryInput, entryOutput.get(), stringOutput))

# Set Row and Column Weight
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.mainloop()
