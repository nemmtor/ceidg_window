from zeep import Client, Settings
import xlwt
import xml.etree.ElementTree as ET

settings = Settings(strict=False, xml_huge_tree=True)
api = 'http://datastore.ceidg.gov.pl/CEIDG.DataStore/services/'
api += 'DataStoreProvider201901.svc?singleWsdl'

client = Client(api, settings=settings)
token = 'xCPw8Jxe/E+czZVIEPUPZaZb5SZx+itfymdEe5BxdSrOZS+5SunR93+hi/pXePb8'


dataOd = '2019-11-06'
dataDo = '2019-11-06'

response = client.service.GetMigrationData201901(
    token, DateFrom=dataOd, DateTo=dataDo, City=['Toruń'])

root = ET.fromstring(response)

# Excel
class Excel:
    def __init__(self):
        self.wb = xlwt.Workbook()
        self.sheet = self.wb.add_sheet('Wynik', cell_overwrite_ok=True)
        self.sheet.write(0, 0, 'NIP')
        self.sheet.write(0, 1, 'Firma')
        self.sheet.write(0, 2, 'Imię i nazwisko')
        self.sheet.write(0, 3, 'Telefon')
        self.sheet.write(0, 4, 'Mail')
        self.sheet.write(0, 5, 'Miejscowość')
        self.sheet.write(0, 6, 'Województwo')
        self.sheet.write(0, 7, 'Data rozpoczęcia')
        self.sheet.write(0, 8, 'Status')
        self.sheet.write(0, 9, 'PKD')
    def saveCustomerDetails(self, x, **kwargs):
        self.sheet.write(x, 0, kwargs['nip'])
        self.sheet.write(x, 1, kwargs['firma'])
        self.sheet.write(x, 2, kwargs['imnaz'])
        self.sheet.write(x, 3, kwargs['telefon'])
        self.sheet.write(x, 4, kwargs['mail'])
        self.sheet.write(x, 5, kwargs['miejsc'])
        self.sheet.write(x, 6, kwargs['woj'])
        self.sheet.write(x, 7, kwargs['data_rozp'])
        self.sheet.write(x, 8, kwargs['status'])
        self.sheet.write(x, 9, kwargs['pkd'])
    def saveFile(self):
        self.wb.save(f'wyniki/plik.xls')

excel = Excel()



x=0

for klient in root:
    # y = klient.findall('*//')
    # print(y)
    # check = klient.find('./DaneDodatkowe')
    # print(check.findall('*'))
    telefon = klient.find('./DaneKontaktowe/Telefon').text
    if telefon is None:
        continue
    x += 1
    nip = klient.find('./DanePodstawowe/NIP').text
    firma = klient.find('./DanePodstawowe/Firma').text
    imnaz = f'{klient.find("./DanePodstawowe/Imie").text} {klient.find("./DanePodstawowe/Nazwisko").text}'
    mail = klient.find('./DaneKontaktowe/AdresPocztyElektronicznej').text
    miejsc = [miejsc.text for miejsc in klient.findall('./DaneAdresowe//Miejscowosc') if miejsc.text is not None][0]
    woj = [woj.text for woj in klient.findall('./DaneAdresowe//Wojewodztwo') if woj.text is not None][0]
    data_rozp = klient.find('./DaneDodatkowe/DataRozpoczeciaWykonywaniaDzialalnosciGospodarczej').text
    status = klient.find('./DaneDodatkowe/Status').text
    pkd = klient.find('./DaneDodatkowe/KodyPKD').text

    excel.saveCustomerDetails(x, nip=nip, firma=firma, imnaz=imnaz, telefon=telefon, mail=mail, miejsc=miejsc,
     woj=woj, data_rozp=data_rozp, status=status, pkd=pkd)


excel.saveFile()
