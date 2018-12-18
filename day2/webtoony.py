import requests
import bs4

days=["mon","tue","wed","thu","fri","sat","sun"]

for i in days:
    url="https://m.comic.naver.com/webtoon/weekday.nhn?week="+i
    response= requests.get(url)
    stone = bs4.BeautifulSoup(response.text,'html.parser')
    result = stone.select('.toon_name')
    img = stone.find("img")
    img_src = img.get("src")
    
    print(i)
    print(img_src)
    for j in result[:5]:
        print(j.text)

# for e in stone.select('.im_br')
#         imgs.append(e.text)
#         print(e.select_one('img'["src"]))