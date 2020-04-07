import requests
from bs4 import BeautifulSoup
import time
# from antz.models import CardBrand, CardModel, CardTrim, Car

def my_scheduled_job():
  url = "https://bama.ir/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  links = soup.find_all('a', class_="desktop-specific-brand-models-link")
  for link in links:
      try:
        if link['href'] != "#":
              print(link['href'])
              # items = (link['href']).split("/")
              # brand = CardBrand(name =items[2]); brand.save()
              # model = CardModel(name=items[3], brand=brand); model.save()
              # if len(items) == 5:
              #     trim = CarTrim(name=item[4], brand=brand, model=model); trim.save()
              i = 0
              while True:
                i +=1
                r = requests.get("https://bama.ir" + link['href'] + f'/?page={i}')
                if r.url == "https://bama.ir/car":
                  break
                soup = BeautifulSoup(r.content, 'html.parser')
                carlist = soup.find('div',id= "adlist")
                links = carlist.find_all('a', class_="cartitle cartitle-desktop")
                for item in links:
                    print(item['href'])
              break
      except:
          pass
        

