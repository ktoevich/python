import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com').text # получить код с сайта
soup = BeautifulSoup(response, 'html.parser') # извлечение текста
word = soup.find_all(string=lambda t: "life" in t) # функция нахождения слова life
print(word) # вывести цитаты