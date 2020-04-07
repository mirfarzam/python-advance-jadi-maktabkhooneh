import requests
from bs4 import BeautifulSoup
import time
from antz.models import Brand,M odel,Trim,Car

def my_scheduled_job():
  url = "https://bama.ir/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  links = soup.find_all('a', class_="desktop-specific-brand-models-link")
  for link in links:
      try:
        if link['href'] != "#":
              items = (link['href']).split("/")
              brand = items[2]
              print(f'brand is {brand}')
              model = items[3]
              print(f'model is {model}')
              if len(items) == 5:
                  trim = item[4]
                  print(f'trim is {trim}')
              break
      except:
          pass
        
my_scheduled_job()