import requests
from bs4 import BeautifulSoup
import json

player = 'rrtrog1'
url = "https://pubgtracker.com/profile/pc/" + player

querystring = {"region":"agg"}

headers = {
    'Cache-Control': "no-cache",

    }

response = requests.request("GET", url, headers=headers, params=querystring)

soup = BeautifulSoup(response.text, 'html.parser')
scripts = soup.findAll('script')

for script in scripts:
    if 'var playerData' in str(script.string):
        data = str(script.string)

my_data = data.replace('var playerData = ', '')
new_data = my_data.replace(';', '')
null = None

playerData = json.loads(new_data)

#print(playerData)
total_kills = 0
stats = playerData['Stats']
#print(stats)
for season in stats:
    if season['Season'] == "2018-01" and season['Region'] == 'agg':
        season_stats = season['Stats']  
              
        for stat in season_stats:
            
            if stat['label'] == 'Kills':
                
                total_kills += stat['ValueInt']
            # for reg_stats in mode['Stats']:
            #     if reg_stats['label'] == 'Kills':
            #         total_kills += reg_stats['ValueInt']
print(total_kills)
        # table.update_item(
        #     Key={
        #         'player_id': user
        #     }, 
        #     UpdateExpression='SET total_kills = :val1', 
        #     ExpressionAttributeValues={
        #         ':val1': total_kills
                
        #     }
        # )
#time.sleep(3)
