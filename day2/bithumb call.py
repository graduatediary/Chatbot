import requests
import bs4

url = "https://bithumb.com"
response = requests.get(url)
stone = bs4.BeautifulSoup(response.text,'html.parser')
result = stone.select_one('.coin_list')

for coin in result:
    print(result.select('strong'))