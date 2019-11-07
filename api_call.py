from zeep import Client





class Api:
    def __init__(self):
        url = 'http://datastore.ceidg.gov.pl/CEIDG.DataStore/services/'
        url += 'DataStoreProvider201901.svc?singleWsdl'
        self.client = Client(url)

    def apiRequest(self, dateFrom, dateTo, **kwargs):
        return self.client.service.GetMigrationData201901(
            self.token, DateFrom=dateFrom, DateTo=dateTo, **kwargs)

    def validateToken(self, token):
        self.token = token
        errors = ['Wystąpił błąd. Skontaktuj się z dostawcą usługi.',
        'Niewłaściwy identyfikator użytkownika']
        self.response = self.client.service.GetMigrationData201901(self.token)
        if self.response in errors or len(self.response) == 23:
            return False
        else:
            return True

api = Api()
