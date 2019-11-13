import xml.etree.ElementTree as ET
import xlwt


def parseAnswer(answers, withPhones):
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('Wynik', cell_overwrite_ok=True)
        sheet.write(0, 0, 'NIP')
        sheet.write(0, 1, 'Firma')
        sheet.write(0, 2, 'Imię i nazwisko')
        sheet.write(0, 3, 'Telefon')
        sheet.write(0, 4, 'Mail')
        sheet.write(0, 5, 'Miejscowość')
        sheet.write(0, 6, 'Województwo')
        sheet.write(0, 7, 'Data rozpoczęcia')
        sheet.write(0, 8, 'Status')
        sheet.write(0, 9, 'PKD')

        x = 0
        for answer in answers:
            root = ET.fromstring(answer)
            for klient in root:
                telefon = klient.find('./DaneKontaktowe/Telefon').text
                if withPhones:
                    if telefon is None:
                        continue
                x += 1
                nip = klient.find('./DanePodstawowe/NIP').text
                firma = klient.find('./DanePodstawowe/Firma').text
                imnaz = f'{klient.find("./DanePodstawowe/Imie").text} {klient.find("./DanePodstawowe/Nazwisko").text}'
                mail = klient.find('./DaneKontaktowe/AdresPocztyElektronicznej').text
                miejsc = [miejsc.text for miejsc in klient.findall('./DaneAdresowe//Miejscowosc') if miejsc.text is not None]
                if len(miejsc) > 0:
                    miejsc = miejsc[0]
                else:
                    miejsc = ''
                woj = [woj.text for woj in klient.findall('./DaneAdresowe//Wojewodztwo') if woj.text is not None]
                if len(woj) > 0:
                    woj = woj[0]
                else:
                    woj = ''
                data_rozp = klient.find('./DaneDodatkowe/DataRozpoczeciaWykonywaniaDzialalnosciGospodarczej').text
                status = klient.find('./DaneDodatkowe/Status').text
                pkd = klient.find('./DaneDodatkowe/KodyPKD').text

                sheet.write(x, 0, nip)
                sheet.write(x, 1, firma)
                sheet.write(x, 2, imnaz)
                sheet.write(x, 3, telefon)
                sheet.write(x, 4, mail)
                sheet.write(x, 5, miejsc)
                sheet.write(x, 6, woj)
                sheet.write(x, 7, data_rozp)
                sheet.write(x, 8, status)
                sheet.write(x, 9, pkd)
        print(f'Znaleziono: {x}')
        wb.save(f'wyniki/plik.xls')
