# HTML EXTRACTOR
from bs4 import BeautifulSoup
from urllib.request import urlopen
from settings import PROJECT_ROOT
import csv
 
CONTENT = urlopen("https://gist.github.com/Zenexer/af4dd767338d6c6ba662#file-internet-slang-and-emoticons-md").read()
SLANGS_FILE = PROJECT_ROOT + '\\Slangs\\en_slangs.csv'

def extract():
    """
        Extract: Extrae cada palabra (modismo) junto con su significado real correspondiente
        luego los guarda en el directorio (Slangs/en_slangs.csv) como un CSV
    """
    soup = BeautifulSoup(CONTENT)

    td_count = 0
    tr_count = 0
    slangs = {}

    for tr in soup.find_all(name = 'tr'):
        x,y = None,None
        matched = 0
        for td in tr.children:
            if (td_count%6 == 1) and td.string != '\n':
                matched += 1
                if (matched == 1) : x = td.string
                if (matched == 2) : y = td.string
            if matched == 2:
                slangs[x] = y.replace('"','')
            td_count += 1
        td_count = 0
        tr_count += 1

    slangs.pop('Slang')
    slangs.pop(None)
    slangs.pop('/s')

    # SAVING THE DICT INTO A CSV
    with open(SLANGS_FILE, "w") as csvfile:
        writer = csv.DictWriter(csvfile, ['slang', 'meaning'])
        writer.writeheader()
        for key,val in slangs.items():
            writer.writerow({'slang' : key, 'meaning' : val})

def getSlangs():
    """
        Obtiene las palabras (modismos) con su significado.
    """
    slangs = {}
    with open(SLANGS_FILE) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            slangs[row['slang']] = row['meaning']
    return(slangs)
