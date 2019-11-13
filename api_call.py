from zeep import Client, Settings
from config_parser import config





class Api:
    '''Class variables'''
    url = 'http://datastore.ceidg.gov.pl/CEIDG.DataStore/services/'
    url += 'DataStoreProvider201901.svc?singleWsdl'
    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(url, settings=settings)

    def __init__(self):
        # print('Starting API...')
        pass

    def apiRequest(self, dateFrom, dateTo, **kwargs):
        '''Send request to API.'''

        return self.client.service.GetMigrationData201901(
            config.readApiToken(), DateFrom=dateFrom, DateTo=dateTo, **kwargs)

    @classmethod
    def validateToken(cls, token):
        '''Check if given token is correct. Function needs to check if response
        message is in list of error messages from API.'''
        errors = ['Wystąpił błąd. Skontaktuj się z dostawcą usługi.',
        'Niewłaściwy identyfikator użytkownika']
        response = cls.client.service.GetMigrationData201901(token)
        if response in errors or len(response) == 23:
            return False
        else:
            return True

api = Api()
