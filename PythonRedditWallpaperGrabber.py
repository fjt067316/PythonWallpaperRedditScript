import requests
from bs4 import BeautifulSoup
import json
import re

headers = {'user-agent': '/u/_____\'s python bot' }

r = requests.get('https://www.reddit.com/r/wallpaper/hot.json?limit=1000', headers = headers)

#Turn website into text html code

html = BeautifulSoup(r.content, 'html.parser')

# " https://i.redd.it/ .... " put links to wallpaper in array

links = re.findall(r'\bhttps://i.redd.it/\w+.jpg' , html.text)
print(links)

#put all wallpapers in folder

i=0
for i in range(len(links)):
    jpg = requests.get(links[i])
    name = re.findall(r'\bcomments/.....' , html.text)
    path = 'C:/Users/____/Desktop/wallpapers/{}.jpg'.format(name[i][-5:])
    i += 1
    with open( path, 'wb') as f:
        f.write(jpg.content)

else:
    exit()





