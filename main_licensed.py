from window_modules import Auth, Filter, Loading
from config_parser import config
from ceidg_api import api
from verifyLicence import isGenuine
import os
import sys

if not isGenuine:
    '''Run TurboActive if licence is not activated.'''
    os.system("TurboActivate.exe")
    sys.exit()
if isGenuine:
    if not config.checkConfigExists():
        # If config.ini doesnt exist than popup auth window
        auth = Auth('API Token Authorization')
        auth.root.mainloop()
    else:
        config.loadConfig()
        if not api.validateToken(config.readApiToken()):
            # If config.ini exists but token is invalid than popup auth window
            auth = Auth('API Token Authorization')
            auth.root.mainloop()

    # Main App Window
    filter = Filter('Api Filtr Service')
    filter.root.mainloop()
    # if api.startedRequest:
    #     loading = Loading('Loading...')
    #     loading.mainloop()
    #     if api.finishedRequest:
    #         loading.destroy()
