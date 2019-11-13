import tkinter as tk
from .mainWindow import Window
from api_call import api
from parse_answer import parseAnswer
import datetime as dt


class Filter(Window):
    def __init__(self, title):
        super().__init__(title)
        self.createWidgets()
        self.centerWindow(self.root)

    def createWidgets(self):
        # Main Frame
        # Frames
        main_frame = tk.Frame(self.root)
        # Labels
        dateFrom_label = tk.Label(main_frame, text='Data od:')
        dateTo_label = tk.Label(main_frame, text='Data do:')
        # Entries
        self.dateFrom_entry = tk.Entry(
            main_frame, width=10)
        self.dateTo_entry = tk.Entry(
            main_frame, width=10)
        # Buttons
        submit = tk.Button(main_frame, text='Filtruj', width=10,
                           padx=10, font=Window.useFont(12),
                           command=lambda: self.filterRequest())

        # Side frame
        # Frames
        side_frame = tk.Frame(self.root)
        # Vars
        self.filterPkd_var = tk.IntVar(value=0)
        self.filterCity_var = tk.IntVar(value=0)
        self.filterPhone_var = tk.IntVar(value=0)
        # Checkboxes
        filterPkd = tk.Checkbutton(side_frame,
                                   text='Filtruj po\nPKD',
                                   variable=self.filterPkd_var,
                                   font=Window.useFont(8),
                                   command=lambda: self.toggleEntry(
                                       self.pkd_entry, self.filterPkd_var))
        filterCity = tk.Checkbutton(side_frame,
                                    text='Filtruj po\nmiastach',
                                    variable=self.filterCity_var,
                                    font=Window.useFont(8),
                                    command=lambda: self.toggleEntry(
                                        self.city_entry, self.filterCity_var))
        filterPhone = tk.Checkbutton(side_frame,
                                     text='Tylko z\nnumerami',
                                     variable=self.filterPhone_var,
                                     font=Window.useFont(8))
        # Entries
        self.pkd_entry = tk.Entry(side_frame, width=10, state="disabled")
        self.city_entry = tk.Entry(side_frame, width=10, state="disabled")

        # Main frame pack
        dateFrom_label.pack()
        self.dateFrom_entry.pack()
        dateTo_label.pack()
        self.dateTo_entry.pack()
        submit.pack(pady=(10, 0))
        main_frame.pack(padx=10, pady=(5, 15), side="left")

        # Side frame pack
        filterPhone.pack()
        filterPkd.pack()
        self.pkd_entry.pack()
        filterCity.pack()
        self.city_entry.pack()
        side_frame.pack(padx=10, pady=(5, 15))

    def filterRequest(self):
        dateFrom = dt.datetime.strptime(
            self.dateFrom_entry.get().strip(), '%Y-%m-%d')
        dateTo = dt.datetime.strptime(
            self.dateTo_entry.get().strip(), '%Y-%m-%d')
        kwargs = {}
        withPhones = False
        if self.filterPhone_var.get():
            withPhones = True
        if self.filterPkd_var.get():
            kwargs['PKD'] = self.pkd_entry.get().strip().split(',')
        if self.filterCity_var.get():
            kwargs['City'] = self.city_entry.get().strip().split(',')
        if (dateFrom.year == dateTo.year) and (dateFrom.month == dateTo.month):
            daysCount = dateTo.day - dateFrom.day
            if dateFrom.month < 10:
                month = f'0{dateFrom.month}'
            else:
                month = dateFrom.month
        answers = []
        if daysCount > 0:
            for day in range(dateFrom.day, dateFrom.day + daysCount + 1):
                if day < 10:
                    day = f'0{day}'

                answers.append(api.apiRequest(
                    f'{dateFrom.year}-{month}-{day}',
                    f'{dateFrom.year}-{month}-{day}',
                    **kwargs))
                print(f'Finished: {dateFrom.year}-{month}-{day}')

        # answer = api.apiRequest(dateFrom, dateTo, **kwargs)
        # # Excel
        parseAnswer(answers, withPhones)
        self.root.destroy()
        # Here some message BOX

    def toggleEntry(self, entry, var):
        if var.get() == 1:
            entry.config(state='normal')
        else:
            entry.config(state='disabled')
