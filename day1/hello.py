# mission 1

# webbrowser, "ssafy","samsung","sw","coding"

# 반복문을 사용하세요.

import webbrowser

A="https://search.daum.net/search?q="
keywords = ["ssafy","samsung","sw","coding"]

for i in keywords:
    webbrowser.open(A+i)
