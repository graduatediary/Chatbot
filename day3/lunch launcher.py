import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

import requests
from time import sleep
import bs4

import time
import re
 
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
    'mon':-1, 'tue': -2, 'wed' : -3, 'thu':-4, 'fri':-5
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

key = "799893065:AAF671iykHhvFZ9X-LUr6wvryRRDnl55JXY"
user_id = "724888484" #강사님꺼
#"224026642" #내꺼

url=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={title}"
url2=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={A}"
url3=f"https://api.telegram.org/bot{key}/sendMessage?chat_id={user_id}&text={B}"

requests.get(url)
requests.get(url2)
requests.get(url3)