import requests
from bs4 import BeautifulSoup
import time
import re
from antz.models import CarBrand, CarModel, CarTrim, URL, Car
from django.db import IntegrityError

def crawlCarPage(url):
  time.sleep(1)
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
      price = None
  spans = (paragraphs[2]).find_all('span')
  str = spans[1].text
  parts = re.findall('[0-9]+', str)
  used = ''.join(parts)
  try:
      used = int(used)
  except:
      used = None
  return year, price, used



def searchCarBrandCarModelLinks():
  url = "https://bama.ir/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  links = soup.find_all('a', class_="desktop-specific-brand-models-link")
  print(len(links))
  return links

def getCarLinks(searchLink):
  i = 0
  links = []
  url_parts = (searchLink).split("/")

  # Get CarBrand
  brand_name = url_parts[2]
  try:
    brand = CarBrand.objects.get(name=brand_name)
  except CarBrand.DoesNotExist:
    brand = CarBrand(name=brand_name);brand.save()

  # Get CarModel
  model_name = url_parts[3]
  try:
    model = CarModel.objects.get(name=model_name, car_brand = brand)
  except CarModel.DoesNotExist:
    model = CarModel(name=model_name, car_brand = brand);model.save()

  trim = None
  if len(url_parts) >= 5 :
    trim_name = url_parts[4]
    try:
      trim = CarTrim.objects.get(name=trim_name, car_brand = brand, car_model = model)
    except CarTrim.DoesNotExist:
      trim = CarTrim(name=trim_name, car_brand = brand, car_model = model);trim.save()

  while True:
    i +=1
    r = requests.get("https://bama.ir" + searchLink + f'/?page={i}')
    if r.url == "https://bama.ir/car":
      break
    soup = BeautifulSoup(r.content, 'html.parser')
    carlist = soup.find('div',id= "adlist")
    tempLinks =  carlist.find_all('a', class_="cartitle cartitle-desktop")
    for item in tempLinks:
      try:
        url_entity = URL.objects.get(url=item['href'])
        continue
      except URL.DoesNotExist:
        url_entity = URL(url = item['href']); url_entity.save()
        links.append(url_entity)
  return brand, model, trim, links

def crawlerTask():
  links = searchCarBrandCarModelLinks()
  for link in links:
      try:
        if link['href'] != "#":
          brand, model, trim, car_links = getCarLinks(link['href'])
          if len(car_links) == 0:
            continue
          for link in car_links:
            year, price, kilometer = crawlCarPage(link.url)
            try:
              car = Car(
                url = link,
                car_brand=brand,
                car_model=model,
                car_trim=trim,
                price=price,
                kilometer=kilometer,
                year=year)
              car.save()
            except IntegrityError:
              pass
            except Exception as e:
              print(e)
              pass
      except Exception as error:
        print(error)