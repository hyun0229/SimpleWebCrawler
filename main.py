import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?sca_esv=ffd3fb7f87e5c6af&q=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&tbm=nws&source=lnms&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ98Z_XVxzNb13fp2atSe3aTaGOl1qnDOvymY5CnPjcs8xMh5-YpODGokwWO0kSnTljeWrrXmZPxYLxfX59BJ_E0HG3h4E-UxEgjPUNQ6U-ktE_aCF4GJ6rD1HMRnQPf5ymCO3lIuAdNM_7pGfY-6Wl1_0ih5y&sa=X&ved=2ahUKEwih_9H4wYqJAxUSsFYBHdGPNPcQ0pQJegQIDBAB&biw=1470&bih=833&dpr=2"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

titles = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')

count = 0
for title in titles:
   count += 1
   print(f"[{count}th", title.get_text())