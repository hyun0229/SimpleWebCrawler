import requests
from bs4 import BeautifulSoup


search = "대한민국" #검색어 설정
num = 3 #페이지 최대 수 설정
count = 0 #기사 개수

for i in range(num): #페이지 수 만큼 반복
    url = "https://www.google.com/search?sca_esv=ffd3fb7f87e5c6af&q="+search+"=nws&ei=p1sLZ-LzHI-m2roPtN2WMA&start="+str(i*10)+"&sa=N&ved=2ahUKEwii46D60IqJAxUPk1YBHbSuBQYQ8tMDegQIARAE&biw=1470&bih=833&dpr=2"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')

    titles = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd') #기사 제목


    for title in titles:
        count += 1
        print(f"[{count}th", title.get_text()) #기사 제목 출력

    print("hello")
