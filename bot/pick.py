import discord
import asyncio
import http.client
import json
import random


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

print(drop_picker('erangel', 'n'))