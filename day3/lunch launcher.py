import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

import requests
from time import sleep
import bs4

import time

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules
 
browser = webdriver.Chrome('/Users/student/Downloads/chromedriver/chromedriver')

browser.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')

id=browser.find_element_by_id('userId')
id.send_keys("tyran88@naver.com")

id=browser.find_element_by_name('userPwd')
id.send_keys("lunchlauncher1!")

menu_submit=browser.find_element_by_class_name('btn')
menu_submit.click()


url = "https://edu.ssafy.com/edu/board/notice/list.do"

browser.get('https://edu.ssafy.com/edu/board/notice/list.do')
browser.find_element_by_xpath('//*[@id="wrap"]/form/div/div[2]/div/div[1]/table[2]/tbody/tr/td[2]/a').click()

every = browser.page_source
stone = bs4.BeautifulSoup(every,'html.parser')
rows = stone.find_all('table')[1].find('tbody').find_all('tr')
rows = rows[2:-2]

menus=[]

today = time.strftime("%a").lower()
params={
    'mon':-5, 'tue': -4, 'wed' : -3, 'thu':-2, 'fri':-1
}

for row in rows:
        cells = row.find_all('td')
        contents = cells[params[f'{today}']].get_text()
        
        menus.append(
            contents
        )

menus.insert(2,"A코스")
title = menus[0:2]
A = menus[2:11]
menus.insert(11,"B코스")
B = menus[11:]
browser.quit()

msg=f"{menus[0]}{menus[1]} 메뉴"
msgA=""
msgB=""
for i in range(2,11):
    msgA=msgA+"\n" + menus[i]
for i in range(11,20):
    msgB=msgB +"\n" + menus[i]
msgC="식사 맛있게 하세요~"
key = "799893065:AAF671iykHhvFZ9X-LUr6wvryRRDnl55JXY"
user_id = "724888484" #내꺼
#"224026642" #강사님꺼

# url=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={msg}"
# url2=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={msgA}"
# url3=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={msgB}"
# url4=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={msgC}"

# requests.get(url)
# requests.get(url2)
# requests.get(url3)
# requests.get(url4)


# message reply function
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)

def menu_command(bot, update) :
    update.message.reply_text(msg+"\n"+msgA+"\n"+msgB+"\n"+msgC)

updater = Updater(key)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

menu_handler = CommandHandler('식단', menu_command)
updater.dispatcher.add_handler(menu_handler)

menu_handler = CommandHandler('menu', menu_command)
updater.dispatcher.add_handler(menu_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()