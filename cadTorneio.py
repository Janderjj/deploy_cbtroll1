import urllib, urllib.parse, urllib.request
import json

api_key = "RGAPI-5a8c30b5-d0bc-41c0-953f-788af715f5a7"
url = 'https://americas.api.riotgames.com/lol/tournament-stub/v5/providers?api_key='+api_key
dados = {"region": "BR1","url": "br1.api.riotgames.com"}

dados = json.dumps(dados)
dados = str(dados)
dados = dados.encode("utf-8")

data = urllib.request.urlopen(url,data=dados)
data = data.read()
print(data)

