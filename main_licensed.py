from window_modules import Auth, Filter
from config_parser import config
from api_call import api
from verifyLicence import isGenuine
import os
import sys

print(isGenuine)
if not isGenuine:
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


    filter = Filter('Api Filtr Service')
    filter.root.mainloop()

else:
    print('Not valid licence!')
