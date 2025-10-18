<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com').text # получить код с сайта
soup = BeautifulSoup(response, 'html.parser') # извлечение текста
word = soup.find_all(string=lambda t: "life" in t) # функция нахождения слова life
=======
import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com').text # получить код с сайта
soup = BeautifulSoup(response, 'html.parser') # извлечение текста
word = soup.find_all(string=lambda t: "life" in t) # функция нахождения слова life
>>>>>>> ae8a85ea4a64b0d6a5559a749d9dd1f2df152bf2
print(word) # вывести цитаты