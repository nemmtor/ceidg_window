import tkinter as tk
from .mainWindow import Window


class Loading(Window):
    def __init__(self, title):
        super().__init__(title)
        self.createWidgets()
        self.centerWindow(self.root)

    def createWidgets(self):
        # Main Frame
        # Frames
        main_frame = tk.Frame(self.root)
        # Labels
        waitlabel = tk.Label(
            main_frame, text='Please wait for API response...')
        waitlabel.pack()
        main_frame.pack(padx=10, pady=(5, 15))
