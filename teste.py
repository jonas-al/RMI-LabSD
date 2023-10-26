import requests
import json 
import climage
from io import BytesIO
from PIL import Image

res = requests.get('https://valorant-api.com/v1/agents')
response = json.loads(res.text)
imgUrl = response['data'][0]['displayIcon']
teste = requests.get(imgUrl)
img = Image.open(BytesIO(teste.content))
converted = climage.convert_pil(img, is_256color=True)
print(converted)

#output = climage.convert('banana.png')
#print(output)

'''agents = []
for agent in response['data']:
    agents.append(agent['displayName'])

print(agents)'''
