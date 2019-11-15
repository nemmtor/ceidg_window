import configparser
import os


class Config():
    '''Create Read Update Delete config files'''

    def loadConfig(self):
        '''Load config from file.'''
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def createConfig(self, token):
        '''Create config file.'''
        self.config = configparser.RawConfigParser()
        self.config.add_section('USER')
        self.config.set('USER', 'apitoken', token)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def readApiToken(self):
        '''Read API token'''
        return self.config['USER']['apitoken']

    @staticmethod
    def checkConfigExists():
        '''Check if config file exists in directory'''
        return os.path.exists('./config.ini')


config = Config()
