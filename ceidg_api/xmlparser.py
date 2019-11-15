import xml.etree.ElementTree as ET
from .excel import Excel


class Parser:
    def __init__(self):
        pass

    def parseAnswer(self, answers, withPhones, withPkd, **kwargs):
        excel = Excel()
        resultCounter = 0
        for answer in answers:
            root = ET.fromstring(answer)
            for klient in root:
                telefon = klient.find('./DaneKontaktowe/Telefon').text
                if withPhones:
                    if telefon is None:
                        continue
                pkd = klient.find('./DaneDodatkowe/KodyPKD').text
                pkdCheck = pkd.split(',')
                if withPkd:
                    if pkdCheck[0] != kwargs['PKD']:
                        continue
                resultCounter += 1
                nip = klient.find('./DanePodstawowe/NIP').text
                firma = klient.find('./DanePodstawowe/Firma').text
                imnaz = f'{klient.find("./DanePodstawowe/Imie").text} {klient.find("./DanePodstawowe/Nazwisko").text}'
                mail = klient.find(
                    './DaneKontaktowe/AdresPocztyElektronicznej').text
                miejsc = [miejsc.text for miejsc in klient.findall(
                    './DaneAdresowe//Miejscowosc') if miejsc.text is not None]
                if len(miejsc) > 0:
                    miejsc = miejsc[0]
                else:
                    miejsc = ''

                woj = [woj.text for woj in klient.findall(
                    './DaneAdresowe//Wojewodztwo') if woj.text is not None]
                if len(woj) > 0:
                    woj = woj[0]
                else:
                    woj = ''
                data_rozp = klient.find(
                    './DaneDodatkowe/DataRozpoczeciaWykonywaniaDzialalnosciGospodarczej').text
                status = klient.find('./DaneDodatkowe/Status').text

                excel.writeData(resultCounter, 0, nip)
                excel.writeData(resultCounter, 1, firma)
                excel.writeData(resultCounter, 2, imnaz)
                excel.writeData(resultCounter, 3, telefon)
                excel.writeData(resultCounter, 4, mail)
                excel.writeData(resultCounter, 5, miejsc)
                excel.writeData(resultCounter, 6, woj)
                excel.writeData(resultCounter, 7, data_rozp)
                excel.writeData(resultCounter, 8, status)
                excel.writeData(resultCounter, 9, pkd)
        excel.saveFile()


parser = Parser()
