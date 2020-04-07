import requests
from bs4 import BeautifulSoup
import time
import re
# from antz.models import CardBrand, CardModel, CardTrim, Car


def crawlCarPage(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.findAll("h1", {"class": "addetail-title"})[0]
    titleSpans = title.find_all('span')
    year = int((titleSpans[-1])['datetime'])
    info = soup.findAll("div", {"class": "inforight"})[0]
    paragraphs = info.find_all('p')
    spans = (paragraphs[0]).find_all('span')
    price = re.sub(',', '', spans[1].text)
    try:
        price = int(price)
    except:
        price = 0
    spans = (paragraphs[2]).find_all('span')
    str = spans[1].text
    parts = re.findall('[0-9]+', str)
    used = ''.join(parts)
    try:
        used = int(used)
    except:
        used = 0
    return year, price, used
  


def searchBrandModelLinks():
  url = "https://bama.ir/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  links = soup.find_all('a', class_="desktop-specific-brand-models-link")
  return links  

def getCarLinks(searchLink):
  i = 0
  links = []
  url_parts = (searchLink).split("/")
  brand = url_parts[2]
  model = url_parts[3]
  trim = None
  if len(url_parts) >= 5 :
    trim = url_parts[4]
  while True:
    i +=1
    r = requests.get("https://bama.ir" + searchLink + f'/?page={i}')
    if r.url == "https://bama.ir/car":
      break
    soup = BeautifulSoup(r.content, 'html.parser')
    carlist = soup.find('div',id= "adlist")
    tempLinks =  carlist.find_all('a', class_="cartitle cartitle-desktop")
    for item in tempLinks:
        links.append(item['href'])
  return brand, model, trim, links

def my_scheduled_job():
  links = searchBrandModelLinks()
  for link in links:
      try:
        if link['href'] != "#":
          brand, model, trim, car_links = getCarLinks(link['href'])          
          for link in car_links:
            year, price, kilometer = crawlCarPage(link)  
            print(f'for the car ')
          break
      except Exception as exception:
          print(exception)
        
my_scheduled_job()
