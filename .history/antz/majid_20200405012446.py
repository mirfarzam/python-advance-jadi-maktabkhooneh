import requests
from bs4 import BeautifulSoup
import time



url = "https://bama.ir/car/{}/{}/?page={}".format(brand, model, i)


while True:
    
    r = requests.get(url)
    if r.url == "https://bama.ir/car":
        break
    soup = BeautifulSoup(r.content, 'html.parser')
    carlist = soup.find('div',id= "adlist")
    links = carlist.find_all('a', class_="cartitle cartitle-desktop")
    for item in links:
        cars.append(item['href'])
    i += 1


print(len(cars))