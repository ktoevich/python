import requests # импортируем библиотеку request для работы с ссылками
response = requests.get('https://api.github.com/user') # получаем информацию о сайте черещ ссылку
print('Статус сайта:', response.status_code) # статус отправки или получения кода
print('Тип контента:',response.headers['content-type']) # тип контента
print('200 смволов Кода', response.text[:200]) # 200 символов а может быть и меньше (в зависимости оттого сколько всего символов в сайте)