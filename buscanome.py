from urllib.request import urlopen

import json
import sys

def verificanome(name,tagname,api_key):
    lista = []
    try:
        
        tier = "oi"
        

        url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+name+'/'+tagname+'?api_key='+api_key
        data = urlopen(url)
        data = data.read()
        print(data)
        data_dict = json.loads(data)
        summer = urlopen('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'+data_dict['puuid']+'?api_key='+api_key)
        summer = summer.read()
        print(summer)
        ret = json.loads(summer)
        lista.append (data_dict['puuid'])
        lista.append(data_dict['gameName'])
        lista.append(data_dict['tagLine'])
        lista.append(ret['id'])
        lista.append(ret['accountId'])
        lista.append(ret['profileIconId'])
        lista.append("https://ddragon-webp.lolmath.net/latest/img/profileicon/"+str(ret['profileIconId'])+".webp")
        lista.append(ret['summonerLevel'])
            
        try: 
            ranked_url ='https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+ret['id']+'?api_key='+api_key
            data_ranked = urlopen(ranked_url)
            data_ranked = data_ranked.read()
            print(data_ranked)
            data_ranked = json.loads(data_ranked)
            data_ranked = data_ranked[0]
        
            lista.append(data_ranked['tier'])
            lista.append(data_ranked['rank'])
        except:
            lista.append('UNRANKED')        
    except:
        lista.append('NÃO ENCONTRADO')  
    return(lista)

    
