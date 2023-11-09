from tkinter import Frame, Label, Entry, Button
from define import *

class MyFrame(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self['bg']      = '#F8F9F9'
        self.grid(row = 0, padx = 2)

class MyLabel(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['fg']      = 'Black'
        self['bg']      = '#F8F9F9'
        self['font']    = FONT_DEFAULT

        self.grid(row = 0, column = 0, sticky = NW, padx = 10)

class MyEntry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self['bg']      = '#A3E4D7'
        self['font']    = FONT_DEFAULT

        self.grid(row = 1, column = 0, padx = 10)

class MyButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['activebackground']    = 'Black'
        self['font']                = FONT_DEFAULT

        self.grid(row = 2, column= 0, sticky = SE, pady = 10, padx = 10)
