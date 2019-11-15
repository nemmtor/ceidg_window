import xlwt
import tkinter as tk
import tkinter.filedialog as filedialog
import os


class Excel:
    def __init__(self):
        self.wb = xlwt.Workbook()
        self.addSheet('Wynik filtru')
        self.addColumns()

    def addSheet(self, sheetName):
        self.sheet = self.wb.add_sheet(sheetName, cell_overwrite_ok=True)

    def addColumns(self):
        self.sheet.write(0, 0, 'NIP')
        self.sheet.write(0, 1, 'Firma')
        self.sheet.write(0, 2, 'Imię i nazwisko')
        self.sheet.write(0, 3, 'Telefon')
        self.sheet.write(0, 4, 'Mail')
        self.sheet.write(0, 5, 'Miejscowość')
        self.sheet.write(0, 6, 'Województwo')
        self.sheet.write(0, 7, 'Data rozpoczęcia')
        self.sheet.write(0, 8, 'Status')
        self.sheet.write(0, 9, 'PKD')

    def writeData(self, row, column, data):
        self.sheet.write(row, column, data)

    def saveFile(self):
        root = tk.Tk()
        root.withdraw()
        filePath = filedialog.asksaveasfilename(initialdir=os.path.expanduser(
            "~/Desktop"),
            title="Select file",
            filetypes=[
            ("Plik excel", "*.xls")],
            defaultextension="*.xls")
        self.wb.save(filePath + '.xls')
        root.destroy()
