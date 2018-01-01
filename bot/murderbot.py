import discord
import asyncio
import http.client
import json
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!murderboard'):

        conn = http.client.HTTPSConnection("uprbu535he.execute-api.us-east-1.amazonaws.com")

        headers = {
            'Cache-Control': "no-cache",
            }

        conn.request("GET", "/prod/players", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        data = sorted(data, key=lambda k: k['total_kills'], reverse=True) 

        msg = "{0:<20} {1:>10}".format("Player ID", "Total Murders \n" + "-"*35+'\n')
        for player in data:
            msg += "{0:<20} {1:>10}".format(player['player_id'], str(int(player['total_kills'])))
            msg += '\n'
        msg = "```" + msg + "```"
        print(msg)
        
        await client.send_message(message.channel, msg)
    elif message.content.lower() == 'who is numba 1?':
        conn = http.client.HTTPSConnection("uprbu535he.execute-api.us-east-1.amazonaws.com")

        headers = {
            'Cache-Control': "no-cache",
            }

        conn.request("GET", "/prod/players", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        data = sorted(data, key=lambda k: k['total_kills'], reverse=True)
        msg = data[0]['player_id'] + " is numba 1!!!! with " + str(int(data[0]['total_kills'])) + ' murders' 
        await client.send_message(message.channel, msg)
#bot token  required in following line, removed for security        
client.run('token')
