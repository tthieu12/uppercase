import os
from tkinter import *
# Set Geometry
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_POSITION_RIGHT = 400
WINDOW_POSITION_DOWN = 200

# Set Images
PATH_DIRECTORY = os.path.dirname(__file__)
PATH_IMAGES = os.path.join(PATH_DIRECTORY, 'images')

# Set Color
COLOR_BACKGROUND = '#76D7C4'

# Set Font
FONT_DEFAULT = ('Palatino', 20)

# Set Entry Placeholder
stringInput = 'lowercase input'
stringOutput = 'uppercase output'