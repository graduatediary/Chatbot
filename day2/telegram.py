import requests
from time import sleep
import bs4


url = "https://www.naver.com"
response = requests.get(url)
result = bs4.BeautifulSoup(response.text,'html.parser')
value = result.select_one('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k'  )

key = "799893065:AAF671iykHhvFZ9X-LUr6wvryRRDnl55JXY"
user_id = "724888484"
message= value.text
#"Hope is a good thing, maybe the best of things, and no good thing ever dies."
#"224026642"

url=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={message}"

while True:
    sleep(1)
    requests.get(url)
