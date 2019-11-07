from window import Window
import tkinter as tk
from config import font12
from api_call import api


class Auth(Window):
    def createWidgets(self):
        main_frame = tk.Frame(self.root)
        token_label = tk.Label(main_frame, text='Token:')
        self.token_entry = tk.Entry(
            main_frame, width=30)
        submit = tk.Button(main_frame, text='Sprawdź token', width=10,
                           padx=10, font=font12,
                           command=lambda: self.checkToken())

        token_label.pack()
        self.token_entry.pack()
        submit.pack(pady=(10, 0))
        main_frame.pack(padx=10, pady=(5, 15))

    def checkToken(self):
        if api.validateToken(self.token_entry.get().strip()):
            # Here some message BOX
            self.root.destroy()
        else:
            # Here some message BOX
            print('Error!')
