import os
from define import *
class App:
    def __init__(self, root):
        #root.resizable(False, False)
        # Set Titile
        root.title('Lower  to Upper')

        # Set Geometry
        root.geometry('{}x{}+{}+{}'.format(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_POSITION_RIGHT,WINDOW_POSITION_DOWN))

        # Set Background
        root['bg'] = COLOR_BACKGROUND

        # Set Icon
        root.iconbitmap(os.path.join(PATH_IMAGES, 'icon.icns'))

        # Min and Max Size
        root.minsize(500, 300)
        root.maxsize(900, 600)