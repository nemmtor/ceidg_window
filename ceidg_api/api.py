from zeep import Client, Settings
from config_parser import config
from .xmlparser import parser


class Api:
    '''Class variables'''
    url = 'http://datastore.ceidg.gov.pl/CEIDG.DataStore/services/'
    url += 'DataStoreProvider201901.svc?singleWsdl'
    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(url, settings=settings)

    def __init__(self):
        self.startedRequest = False
        self.finishedRequest = False

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

    def filterRequest(self, dateFrom, dateTo, withPhones, withPkd, dataPkd):
        self.startedRequest = True
        kwargs = {}
        if withPkd:
            kwargs['PKD'] = dataPkd
        answers = []
        # Request for every day
        if (dateFrom.year == dateTo.year) and (dateFrom.month == dateTo.month):
            daysCount = dateTo.day - dateFrom.day
            if dateFrom.month < 10:
                month = f'0{dateFrom.month}'
            else:
                month = dateFrom.month
            for day in range(dateFrom.day, dateFrom.day + daysCount + 1):
                if day < 10:
                    day = f'0{day}'

                answers.append(self.apiRequest(
                    f'{dateFrom.year}-{month}-{day}',
                    f'{dateFrom.year}-{month}-{day}',
                    **kwargs))
                print(f'Finished: {dateFrom.year}-{month}-{day}')
        self.finishedRequest = True
        parser.parseAnswer(answers, withPhones, withPkd, **kwargs)
