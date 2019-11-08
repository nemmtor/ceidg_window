import tkinter as tk
from .mainWindow import Window
from api_call import api
from parse_answer import parseAnswer


class Filter(Window):
    def __init__(self, title):
        super().__init__(title)
        self.createWidgets()


    def createWidgets(self):
        main_frame = tk.Frame(self.root)
        dateFrom_label = tk.Label(main_frame, text='Data od:')
        self.dateFrom_entry = tk.Entry(
            main_frame, width=10)
        dateTo_label = tk.Label(main_frame, text='Data do:')
        self.dateTo_entry = tk.Entry(
            main_frame, width=10)
        submit = tk.Button(main_frame, text='Filtruj', width=10,
                           padx=10, font=Window.useFont(12),
                           command=lambda: self.filterRequest())

        dateFrom_label.pack()
        self.dateFrom_entry.pack()
        dateTo_label.pack()
        self.dateTo_entry.pack()
        submit.pack(pady=(10, 0))
        main_frame.pack(padx=10, pady=(5, 15))

    def filterRequest(self):
        dateFrom = self.dateFrom_entry.get().strip()
        dateTo = self.dateTo_entry.get().strip()
        answer = api.apiRequest(dateFrom, dateTo)
        parseAnswer(answer)
        self.root.destroy()
        # Here some message BOX
