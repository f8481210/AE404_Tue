import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.books.com.tw/web/sys_saletopb/books")

soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all("div", class_="type02_bd-a")

#print(divs) #divs是list

for i in divs:
    h4 = i.find("h4")
    if not h4:
        continue
    a = i.find("a")
    if not a:
        continue
    name = a.text
    print(name)