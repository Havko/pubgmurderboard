import discord
import asyncio
import http.client
import json
import random
client = discord.Client()

def drop_picker(location, vicinity):
    locations = []
    erangel ={
    "se" : [
        "Novo", "Military", "Military Island Southern Coast", "Military Island Northern Coast", "Power",
         "Factory", "Mylta", "Farm", "Prison", "Shelter", "Lipovka", "Eastern Military Bridge island side",
          "Eastern Military Bridge mainland side" 
        ],
    "ne" : ["Kameshki", "Stalber", "Northeastern Coast", "Mansion", "Yasnaya Pooolyannnaaaaa", "School"],
    "nw" : ["Zharki is love, Zharki is life", "Severny", "Shooting Range", "North George", "South George",
     "Georgie Containers", "Hospital", "Sunken City", "Ruins", "Rozhok" 
     ],
    "sw" : ["Southwestern Coast", "Western Military Coast", "Ferry", "Quarry", "Gatka" "Pochinki", "Western Military Bridge Mainland", "Western Military Bridge island side"]
    }

    miramar= {
    "nw" : ["Ruins", "Trailer Park", "La Cobreria", "Crater Fields", "El Pozo", "San Martin", "Monte Nuevo", "Power Grid"],
    "ne" : ["Campo Militar", "Torre Ahumada", "Cruz del Valle", "Tierra Bronca", "El Azahar", "Junkyard", "Graveyard", "Minas Generales", "Hacienda", "Water Treatment"],
    "sw" : ["Prison", "Minas del Sur", "Los Higos", "Valle del Mar", "Minas del Valle", "Chumacera", "Ladrillera", "Pecado", "Small easter prison island"],
    "se" : ["Eastern Islands", "Los Leones", "Puerto Paraiso", "Impala", "La Bendita", "Southeastern Coast"],
    }
    if location == "erangel":
        pick_from = erangel
    elif location == "miramar":
        pick_from = miramar
    else:
        return "Invalid location"
    #
    if vicinity == "s":
        locations = pick_from['se'] + pick_from['sw']
    elif vicinity == "n":
        locations = pick_from['ne'] + pick_from['nw']
    elif vicinity == "w":
        locations = pick_from['nw'] + pick_from['sw']
    elif vicinity == "e":
        locations = pick_from['ne'] + pick_from['se']
    else:
        locations = pick_from[vicinity]

    random.shuffle(locations)
    return locations.pop()
    
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

        msg = "{0:<15} {1:^15} {2:>15}".format("Player ID", "Total Murders", "Chicken Dinners \n" + "-"*50+'\n')
        for player in data:
            msg += "{0:<17} {1:^10} {2:>10}".format(player['player_id'],str(int(player['total_kills'])), str(int(player['chicken_dinners'])))
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
    
    elif 'where should we drop' in message.content.lower():
        msg = message.content.lower()
        
        if 's miramar' in msg:
            vicinity = 's'
            location = 'miramar'
        elif 'n miramar' in msg:
            vicinity = 'n'
            location = 'miramar'
        elif 'e miramar' in msg:
            vicinity = 'e'
            location = 'miramar'
        elif 'w miramar' in msg:
            vicinity = 'w'
            location = 'miramar'
        elif 'se miramar' in msg:
            vicinity = 'se'
            location = 'miramar'
        elif 'sw miramar' in msg:
            vicinity = 'sw'
            location = 'miramar'
        elif 'ne miramar' in msg:
            vicinity = 'ne'
            location = 'miramar'
        elif 'nw miramar' in msg:
            vicinity = 'nw'
            location = 'miramar'
        elif 's erangel' in msg:
            vicinity = 's'
            location = 'erangel'
        elif 'n erangel' in msg:
            vicinity = 'n'
            location = 'erangel'
        elif 'e erangel' in msg:
            vicinity = 'e'
            location = 'erangel'
        elif 'w erangel' in msg:
            vicinity = 'w'
            location = 'erangel'
        elif 'se erangel' in msg:
            vicinity = 'se'
            location = 'erangel'
        elif 'sw erangel' in msg:
            vicinity = 'sw'
            location = 'erangel'
        elif 'ne erangel' in msg:
            vicinity = 'ne'
            location = 'erangel'
        elif 'nw erangel' in msg:
            vicinity = 'nw'
            location = 'erangel'
        new_msg = drop_picker(location, vicinity)
        await client.send_message(message.channel, new_msg)        
#bot token  required in following line, removed for security        
client.run('')
