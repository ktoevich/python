import requests # импорт модуля
params = { # создание множества
    'name' : 'Шерзод',
    'city' : 'Душанбе'
}
headers = { # множество для юсер агента
    'User-Agent' : 'agentusera'
}
response = requests.get('https://httpbin.org/get', params=params, headers=headers).json() # получение данных как json 
print(response['name']) # вывод имени
print(response['city']) # вывод города
print(response['User-Agent']) # вывод юсер агента

# Оно не работает потому что ты не правильно обращаешься к аргументами пропуская ключь первого уровня. нужно было написать что то на подобии response['args']['name'] и response['args']['city'] и response['headers']['User-Agent']