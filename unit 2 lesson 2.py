<<<<<<< HEAD
import requests
params = {
    'name' : 'Шерзод',
    'city' : 'Душанбе'
}
headers = {
    'User-Agent' : 'agentusera'
}
response = requests.get('https://httpbin.org/get', params=params, headers=headers).json()
print(response['name'])
print(response['city'])
print(response['User-Agent'])
=======
import requests # импорт модуля
params = { # создание множества
    'name' : 'Шерзод',
    'city' : 'Душанбе'
}
headers = { # множество для юсер агента
    'User-Agent' : 'agentusera'
}
response = requests.get('https://httpbin.org/get', params=params, headers=headers).json() # получение данных как json 
print(response['args']['name']) # вывод имени
print(response['args']['city']) # вывод города
print(response['args']['User-Agent']) # вывод юсер агента


# Оно не работает потому что ты не правильно обращаешься к аргументами пропуская ключь первого уровня. нужно было написать что то на подобии response['args']['name'] и response['args']['city'] и response['headers']['User-Agent']
>>>>>>> ae8a85ea4a64b0d6a5559a749d9dd1f2df152bf2
