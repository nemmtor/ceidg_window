import tkinter as tk
import sys
from config import icon, font12




class Window:
    def __init__(self):
        '''Ustawienie tytułu, rozmiaru'''
        self.root = tk.Tk()
        self.root.title('Company Filter Tool')
        self.root.option_add('*Dialog.msg.font', font12)
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.przycisk_x())
        self.root.pack_propagate(1)
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                       tk.PhotoImage(file=icon))
        self.createWidgets()
        self.centerWindow(self.root)
        self.root.mainloop()  # główny loop

    def centerWindow(self, window, isroot=True):
        '''Ustawienie na środku ekranu oraz ikonka.'''

        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def przycisk_x(self):
        warning_window = tk.Toplevel()
        warning_window.grab_set()
        warning_window.title("Uwaga")
        warning_label = tk.Label(warning_window,
                                 text=("Czy napewno chcesz wyłączyć program?"))
        warning_label.pack()
        ok_butt = tk.Button(warning_window, text='Tak',
                            width=12, padx=10, font=font12,
                            command=lambda: sys.exit())
        ok_butt.pack(side=tk.LEFT, padx=(40, 5), pady=(10, 0))
        cancel_butt = tk.Button(warning_window,
                                text='Anuluj', width=12, padx=10,
                                font=font12,
                                command=lambda: warning_window.destroy())
        cancel_butt.pack(side=tk.RIGHT, padx=(5, 40), pady=(10, 0))
        self.centerWindow(warning_window, False)

# window = Window()
