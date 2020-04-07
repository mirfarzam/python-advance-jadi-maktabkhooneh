import requests
from bs4 import BeautifulSoup
import time
# from models import *

url = "https://bama.ir/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a', class_="desktop-specific-brand-models-link")
for link in links:
    try:
       if link['href'] != "#":
            items = (link['href']).split("/")
            brand = items[2]
            model = items[3]
            if len(items) = 5:
                trim = 
            break
    except:
        pass