import requests
from bs4 import BeautifulSoup
import html5lib
from urllib.parse import urljoin

def ipCheck(value):

    URL = 'https://whatismyipaddress.com/ip/'

    comUrl = urljoin(URL,value)

    r = requests.get(comUrl)
    soup = BeautifulSoup(r.content,'html5lib')
    table = soup.findAll('table')[1]
    table_row = table.findAll('tr')
    print(table_row[1].text)


ans =  input('Enter the IP address:  ')
ipCheck(ans)


