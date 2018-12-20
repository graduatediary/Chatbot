# open('파일명','뭘할지', '[인코딩]')
f = open('names.txt','a',encoding='utf-8')
f.write('\nKorean')
f.closes()

## 영구적(손실 없이)으로 데이터를 저장할 때

# .txt(텍스트)파일 연다
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫는다.

# .json 파일을 연다. (import json) -> dictionary

# .csv 파일을 연다. (import csv) -> 2D list

# with keyword 활용해 코드 간결히 쓰기

# DB 열고(connect) -> CRUD
# 1. 읽기(CREATE)
# 2. 쓰기(READ / RETRIEVE)
# 3. 수정하기(UPDATE)
# 4. 삭제(DELETE / DESTROY)
# DB 닫기(disconnect)

# ORM -> 데이터베이스 가볍게 다루는 거