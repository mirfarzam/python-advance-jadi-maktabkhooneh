import requests
from bs4 import BeautifulSoup
import time

url = "https://bama.ir/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a', class_="desktop-specific-brand-models-link")
for item in links:
    try
    print(item['href'])