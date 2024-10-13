import requests
from bs4 import BeautifulSoup


search = "대한민국"
num = 3
count = 0

for i in range(num):
    url = "https://www.google.com/search?sca_esv=ffd3fb7f87e5c6af&q="+search+"=nws&ei=p1sLZ-LzHI-m2roPtN2WMA&start="+str(i*10)+"&sa=N&ved=2ahUKEwii46D60IqJAxUPk1YBHbSuBQYQ8tMDegQIARAE&biw=1470&bih=833&dpr=2"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')

    titles = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')


    for title in titles:
        count += 1
        print(f"[{count}th", title.get_text())
