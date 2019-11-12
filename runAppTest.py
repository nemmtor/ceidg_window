from window_modules import Auth, Filter
from config_parser import config
from api_call import api

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


filter = Filter('Podaj parametry wyszukiwania')
filter.root.mainloop()
