from zeep import Client, Settings
from config_parser import config
from .xmlparser import parser
import datetime as dt
from calendar import monthrange


class Api:
    '''Class variables'''
    url = 'http://datastore.ceidg.gov.pl/CEIDG.DataStore/services/'
    url += 'DataStoreProvider201901.svc?singleWsdl'
    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(url, settings=settings)

    def __init__(self):
        self.startedRequest = False
        self.dateFrom = ''
        self.dateTo = ''
        self.withPhones = ''
        self.withPkd = ''
        self.pkdData = ''
        self.withStatus = 0
        # test = Api.client.get_element('ns0:GetMigrationData201901')
        # self.status = test(status=[1, 2])
        # print(self.status)

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

    def filterRequest(self):
        dateFrom = dt.datetime.strptime(
            self.dateFrom, '%Y-%m-%d')
        dateTo = dt.datetime.strptime(
            self.dateTo, '%Y-%m-%d')
        kwargs = {}
        if self.withPkd:
            kwargs['PKD'] = self.pkdData
        if self.withStatus:
            kwargs['status'] = 1
            # kwargs['status'] = self.status
        answers = []
        # Request for every day
        if (dateFrom.year == dateTo.year) and (dateFrom.month == dateTo.month):
            print('Method 1')
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

        elif (dateFrom.year == dateTo.year) and not (dateFrom.month == dateTo.month):
            dates = []
            monthsCount = dateTo.month - dateFrom.month
            # First month
            month = dateFrom.month
            if month < 10:
                month = f'0{month}'
            for day in range(dateFrom.day, monthrange(dateFrom.year, int(month))[1] + 1):
                if day < 10:
                    day = f'0{day}'
                date = f'{dateFrom.year}-{month}-{day}'
                dates.append(date)
            # Next months
            if monthsCount > 1:
                for month in range(dateFrom.month+1, dateTo.month):
                    if month < 10:
                        month = f'0{month}'
                    for day in range(1, monthrange(dateFrom.year, int(month))[1] + 1):
                        if day < 10:
                            day = f'0{day}'
                        date = f'{dateFrom.year}-{month}-{day}'
                        dates.append(date)
            # Last month
            month = dateTo.month
            if month < 10:
                month = f'0{month}'
            for day in range(1, dateTo.day + 1):
                if day < 10:
                    day = f'0{day}'
                date = f'{dateTo.year}-{month}-{day}'
                dates.append(date)
            for date in dates:
                print(f'Starting: {date}')
                answers.append(self.apiRequest(
                    date,
                    date,
                    **kwargs))
                print(f'Finished')
        parser.parseAnswer(answers, self.withPhones, self.withPkd, **kwargs)
