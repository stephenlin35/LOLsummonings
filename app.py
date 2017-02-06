import requests

summoner_name = input('Summoner Name: ')
region = input('Region: ')
api_key = input("API_KEY: ")

url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/by-name/' + summoner_name + '?api_key=' + api_key
res = requests.get(url)
res_json = res.json()

print(res_json)
