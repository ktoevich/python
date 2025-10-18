<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com').text # получить код с сайта
soup = BeautifulSoup(response, 'html.parser') # извлечение текста
block = soup.find_all('span', class_='text') # найти цитаты
print(block) # вывести цитаты   
=======
import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com').text # получить код с сайта
soup = BeautifulSoup(response, 'html.parser') # извлечение текста
block = soup.find_all('span', class_='text') # найти цитаты
print(block) # вывести цитаты
>>>>>>> ae8a85ea4a64b0d6a5559a749d9dd1f2df152bf2
