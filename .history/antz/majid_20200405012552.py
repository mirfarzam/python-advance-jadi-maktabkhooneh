import requests
from bs4 import BeautifulSoup
import time

url = "https://bama.ir/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
    links = carlist.find_all('a', class_="cartitle cartitle-desktop")
for item in links:
    cars.append(item['href'])