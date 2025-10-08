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
