import tkinter as tk
from tkinter import messagebox
from api_call import api
from .mainWindow import Window
from config_parser import config


class Auth(Window):
    def __init__(self, title):
        super().__init__(title)
        self.createWidgets()
        self.centerWindow(self.root)


    def createWidgets(self):
        '''Create Frames, labels, entries, buttons etc.'''
        # Frames
        main_frame = tk.Frame(self.root)
        # Labels
        token_label = tk.Label(main_frame, text='Token:')
        # Entries
        self.token_entry = tk.Entry(
            main_frame, width=30)
            # Buttons
        submit = tk.Button(main_frame, text='Sprawdź token', width=10,
                           padx=10, font=Window.useFont(12),
                           command=lambda: self.checkToken(self.token_entry.get().strip()))

        # Pack
        token_label.pack()
        self.token_entry.pack()
        submit.pack(pady=(10, 0))
        main_frame.pack(padx=10, pady=(5, 15))

    def checkToken(self, token):
        '''Check if given token is correct.'''
        if api.validateToken(token):
            config.createConfig(token)
            messagebox.showinfo('Sukces', 'Poprawny token.')
            self.root.destroy()
        else:
            # Here some message BOX
            messagebox.showinfo('Error', 'Niepoprawny token.')
