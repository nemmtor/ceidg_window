import tkinter as tk
import sys
import os


class Window:
    '''Parent class to inherit from'''

    def __init__(self, title):
        '''Create window and set options.'''
        self.root = tk.Tk()
        self.root.title(title)
        self.root.option_add('*Dialog.msg.font', Window.useFont(12))
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.xButton())
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                          tk.PhotoImage(file=self.getIcon('./logo.png')))

    def centerWindow(self, window):
        '''Move window to center.'''
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def xButton(self):
        '''Make X button to popup warning message.'''
        warning_window = tk.Toplevel()
        warning_window.grab_set()
        warning_window.title("Uwaga")
        warning_label = tk.Label(warning_window,
                                 text=("Czy napewno chcesz wyłączyć program?"))
        warning_label.pack()
        ok_butt = tk.Button(warning_window, text='Tak',
                            width=12, padx=10,
                            command=lambda: sys.exit())
        ok_butt.pack(side=tk.LEFT, padx=(40, 5), pady=(10, 0))
        cancel_butt = tk.Button(warning_window,
                                text='Anuluj', width=12, padx=10,
                                command=lambda: warning_window.destroy())
        cancel_butt.pack(side=tk.RIGHT, padx=(5, 40), pady=(10, 0))
        self.centerWindow(warning_window)

    @staticmethod
    def useFont(size):
        '''Use Font based on given size.'''
        return ('Arial 500', size)

    def getIcon(self, relative_path):
        '''Get absolute path to resource, works for dev and for PyInstaller.'''
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')
        return os.path.join(base_path, relative_path)
