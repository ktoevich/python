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