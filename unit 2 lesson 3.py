import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com').text # получить код с сайта
soup = BeautifulSoup(response, 'html.parser') # извлечение текста
block = soup.find_all('span', class_='text') # найти цитаты
print(block) # вывести цитаты