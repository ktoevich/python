<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
text = []
response =requests.get('https://lenta.ru').text
soup = BeautifulSoup(response, 'html.parser')
div_text = soup.find('h3').text
print(div_text)
for h3 in soup.find_all('h3'):
    text.append(h3.text)
print(text)
=======
import requests
from bs4 import BeautifulSoup
text = []
response =requests.get('https://lenta.ru').text
soup = BeautifulSoup(response, 'html.parser')
div_text = soup.find('h3').text
print(div_text)
for h3 in soup.find_all('h3'):
    text.append(h3.text)
print(text)


#  Хахаха я даже испугался прочитав про Израель и Хамас. а ловко ты это придумал...
>>>>>>> ae8a85ea4a64b0d6a5559a749d9dd1f2df152bf2
