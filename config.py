import os
import sys

build = False

# Fonts
font12 = ('Arial 500', 12)
#   Dla odpowiedniego dodania plików do wersji exe
def resource_path(relative_path):
    '''Get absolute path to resource, works for dev and for PyInstaller.'''
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)

if not build:
    icon = resource_path('./pliki/logo.png')


else:
    icon = resource_path('logo.png')
