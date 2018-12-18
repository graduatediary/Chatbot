# 1. python에게 naver.com 요청해서 보내고
# 2. 응답 받은 문서를 저장하고
# 3. BeautifulSoup 정보를 찾기 좋게 만들고
# 4. 우리가 원하는 정보를 뽑아온다.

import requests
import bs4
import webbrowser

url = "https://www.naver.com"

response = requests.get(url)

print(response)
stone = bs4.BeautifulSoup(response.text,'html.parser')
result = stone.select_one('.ah_k')

print(result.text)

searchURL = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
webbrowser.open(searchURL+result.text)