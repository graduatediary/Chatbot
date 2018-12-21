import os
import requests

token = os.getenv('TELEGRAM_TOKEN')
msg = input()

# 상세서: 텔레그램 메시지를 보낸다.
# ------chat_id 받아오는 기능 -----
# 1. 환경 변수 불러와
# - token 환경변수 불러와.
# 2. URL 받고
# 3. getUpdates
# 4. chat_id를 받고
# -------message 보내는 기능--------
# 5. message를 보내는 과정
# 6. 메시지를 보냄.

def getID():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    doc = response.json()
    chat_id=doc['result'][0]['message']['chat']['id']
    
    return chat_id

def sendMessage(chat_id,msg):
    url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    
    return f"{msg}를 {chat_id}님에서 보냈습니다."

chat_id=getID()
sendMessage(chat_id,msg)