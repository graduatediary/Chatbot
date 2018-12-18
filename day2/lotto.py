# 0. random으로 로또 번호를 생성한다.
# 1. 나눔 로또 api를 통해 우승 번호를 가져온다.
# 2. random으로 생성된 번호와 우승 번호를 비교해서 나의 등수를 알려준다.

# 1등 6개 다 맞아야
# 2등 5개 맞고 보너스 번호
# 3등 5개
# 4등 4개
# 5등 3개
# 1억번 돌려보자

import json
import bs4
import requests
import random

url = "https://zzu.li/lotto-api"
response = requests.get(url)
lotto = json.loads(response.text)
winner=[]

for i in range(1,7):
    winner.append(lotto[f"drwtNo{i}"])

print(winner)

def pickLotto():


# count=0
# for i in pick:
#         if i in lotto:
#                 count=count+1
# print(count)

        pick = sorted(random.sample(range(1,47),6))

        A = set(pick)
        B = set(winner)
        C = A & B
        count = len(C)
        print(f"union : {C}")
        print(f"count: {count}")
        print(lotto["bnusNo"])

        if count == 6:
                print("1등!")
        elif count == 5:
                if lotto["bnusNo"] in pick:
                        print("2등!")
                else:
                        print("3등")
        elif count == 4:
                print("4등")
        elif count == 3:
                print("5등")
        else:
                print("꽝!")

for i in range(10):
        pickLotto()