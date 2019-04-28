#1. Получить количество учеников с сайта geekbrains.ru:
#a) при помощи регулярных выражений,
#b) при помощи библиотеки BeautifulSoup.


import re
from bs4 import BeautifulSoup as BS


def get_with_BS():
    with open("c:\index1.html", encoding='utf-8') as f:
         s=f.read()

    soup = BS(s,"html.parser")
    span_tags=soup.find_all("span")
    print(span_tags[0].string)


def get_with_re():
    with open("c:\index1.html", encoding='utf-8') as f:
        s=f.read()
    li=re.findall("Нас уже \d \d+ \d+",s)
    print(li)

get_with_BS()
get_with_re()
