import tkinter as tk
from tkinter import messagebox
from .mainWindow import Window
from ceidg_api import api
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
                           command=lambda: self.checkDate())

        # Side frame
        # Frames
        side_frame = tk.Frame(self.root)
        # Vars
        self.filterPkd_var = tk.IntVar(value=0)
        self.filterPhone_var = tk.IntVar(value=0)
        self.filterStatus_var = tk.IntVar(value=0)
        # Checkboxes
        filterPkd = tk.Checkbutton(side_frame,
                                   text='Filtruj po\ngłównym PKD',
                                   variable=self.filterPkd_var,
                                   font=Window.useFont(8),
                                   command=lambda: self.toggleEntry(
                                       self.pkd_entry, self.filterPkd_var))
        filterPhone = tk.Checkbutton(side_frame,
                                     text='Tylko z\nnumerami',
                                     variable=self.filterPhone_var,
                                     font=Window.useFont(8))
        filterStatus = tk.Checkbutton(side_frame,
                                      text="Tylko aktywne",
                                      variable=self.filterStatus_var,
                                      font=Window.useFont(8))
        # Entries
        self.pkd_entry = tk.Entry(side_frame, width=10, state="disabled")

        # Main frame pack
        dateFrom_label.pack()
        self.dateFrom_entry.pack()
        dateTo_label.pack()
        self.dateTo_entry.pack()
        submit.pack(pady=(10, 0))
        main_frame.pack(padx=10, pady=(5, 15), side="left")

        # Side frame pack
        filterPhone.pack()
        filterStatus.pack()
        filterPkd.pack()
        self.pkd_entry.pack()
        side_frame.pack(padx=10, pady=(5, 15))

    def checkDate(self):
        filledGood = False
        try:
            dt.datetime.strptime(
                self.dateFrom_entry.get().strip(), '%Y-%m-%d')
            dt.datetime.strptime(
                self.dateTo_entry.get().strip(), '%Y-%m-%d')
            filledGood = True
        except ValueError:
            filledGood = False
        if filledGood:
            api.dateFrom = self.dateFrom_entry.get().strip()
            api.dateTo = self.dateTo_entry.get().strip()
            api.withPhones = self.filterPhone_var.get()
            api.withPkd = self.filterPkd_var.get()
            api.pkdData = self.pkd_entry.get().strip()
            api.withStatus = self.filterStatus_var.get()
            api.startedRequest = True
            self.root.destroy()
        else:
            messagebox.showinfo('Error', 'Wrong date')

    def toggleEntry(self, entry, var):
        if var.get() == 1:
            entry.config(state='normal')
        else:
            entry.config(state='disabled')
