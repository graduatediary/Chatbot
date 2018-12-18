import requests
import bs4

url = "https://bithumb.com"
response = requests.get(url)
stone = bs4.BeautifulSoup(response.text,'html.parser')

coin_name = stone.select('.sort_coin')
coin = stone.select('.sort_real')

for i in coin_name[:5]:
    print(i.text)
for i in coin[:5]:
    print(i.text)