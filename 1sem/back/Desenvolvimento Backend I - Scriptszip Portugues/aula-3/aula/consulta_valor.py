import requests

reponse = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dados = reponse.json()
taxa_dolar = dados['USDBRL']['bid']
print(f'Taxa do dólar: {taxa_dolar}')