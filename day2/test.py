url = 'https://www.bithumb.com/'

import requests
from bs4 import BeautifulSoup
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('.coin_list tr'):
  name = tag.select_one('td:nth-of-type(1) a strong').text.replace(' NEW',' ').strip()
  price = tag.select_one('td:nth-of-type(2) strong').text
  print(name + " / " + price)
  f = open("./a.txt", 'a+')
  f.write(name + " / " + price + '\n')

  