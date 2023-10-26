import Pyro5.api

import requests
import json
import random
import climage
from io import BytesIO
from PIL import Image


@Pyro5.api.expose
class Valorant(object):
    def getRandomAgent(self):
        res = requests.get('https://valorant-api.com/v1/agents')
        response = json.loads(res.text)

        agents = []
        for agent in response['data']:
            agents.append(agent['displayName'])
        return agents[random.randint(0, len(agents) - 1)]
    
    def getRandomWeapon(self):
        res = requests.get('https://valorant-api.com/v1/weapons')
        response = json.loads(res.text)

        weapons = []
        for weapon in response['data']:
            weapons.append(weapon['displayName'])
        return weapons[random.randint(0, len(weapons) - 1)]
    
    def getRandomAgentIcon(self):
        res = requests.get('https://valorant-api.com/v1/agents')
        response = json.loads(res.text)
        randomAgent = response['data'][random.randint(0, len(response['data'])-1)]
        imgUrl = randomAgent['displayIcon']
        trueImg = requests.get(imgUrl)
        img = Image.open(BytesIO(trueImg.content))
        converted = climage.convert_pil(img, is_256color=True, width=50)
        return [
            randomAgent['displayName'],
            converted
        ]

    def getMethods(self):
        return '1 - Um agente aleatório \n2 - Uma arma aleatória \n3 - Ícone de algum agente'
        

daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(Valorant) # register the greeting maker as a Pyro object
ns.register("valorant.rmi", uri) # register the obj with a name in the name server

print("Ready.")
daemon.requestLoop()