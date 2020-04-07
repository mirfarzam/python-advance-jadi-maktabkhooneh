import requests
from bs4 import BeautifulSoup
import time
from antz.models import *

url = "https://bama.ir/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a', class_="desktop-specific-brand-models-link")
for link in links:
    try:
       if link['href'] != "#":
            items = (link['h'])
            break
    except:
        pass