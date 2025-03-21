import requests
from bs4 import BeautifulSoup

url = 'https://www.infox.ru/archive/2025-03-04#doc349049'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#Вывод главных новостей
news = soup.find_all('div', class_='item')
time = soup.find_all('div', class_='date')

for i in range(len(news)):
    print(f"{news[i].text.strip()} - {time[i].text.strip()}")
