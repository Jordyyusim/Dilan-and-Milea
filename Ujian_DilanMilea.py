import requests


urlprovinsi = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
urlkodepos = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'

dataprovinsi = requests.get(urlprovinsi).json()
datakodepos = requests.get(urlkodepos).json()

provinsiDilan = 'BANTEN'
cityDilan = 'TANGERANG'
districtDilan = 'CISAUK'
urbanDilan = 'SAMPORA'
provinsiMilea = 'JAWA BARAT'
cityMilea = 'BANDUNG'
districtMilea = 'BANDUNG WETAN'
urbanMilea = 'CITARUM'

kodeprovinsi = []
provinsi = []
for data in dataprovinsi.keys():
    kodeprovinsi += [data]
for data in dataprovinsi.values():
    provinsi += [data]

#DILAN
if provinsiDilan in provinsi:
    index = provinsi.index(provinsiDilan)
    indexDilan = kodeprovinsi[index]
for i in datakodepos[indexDilan]:
    if i['urban'] == urbanDilan and i['sub_district'] == districtDilan and i['city'] == cityDilan:
        kodeposDilan = i['postal_code']

#MILEA
if provinsiMilea in provinsi:
    index = provinsi.index(provinsiMilea)
    indexMilea = kodeprovinsi[index]
for j in datakodepos[indexMilea]:
    if j['urban'] == urbanMilea and j['sub_district'] == districtMilea and j['city'] == cityMilea:
            kodeposMilea = j['postal_code']
apikey = 'TZ3iYthSgNh2YWRsY9lOAZ9sPSa0p2Vosoao3ozDj829xXbMOzGxBft2wmo4atbC'
url = f'http://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodeposDilan}/{kodeposMilea}/km'
abc = requests.get(url).json()
JarakDilanMilea = abc['distance']
print(JarakDilanMilea)
print(kodeposDilan)
print(kodeposMilea)

print('Kode Pos lokasi Dilan adalah', kodeposDilan)
print('Kode Pos lokasi Milea adalah', kodeposMilea)
print(f'Jarak Dilan & Milea adalah {JarakDilanMilea} km')









# apikey = 'TOEBmfv9VYGpfHD3VcLabo3dj9lXOCxprlA1pusvcyzEhJEw1XY6L3WAnpFsnavp'
