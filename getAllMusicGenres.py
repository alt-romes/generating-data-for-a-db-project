import requests
everynoisetext = requests.get('http://everynoise.com/everynoise1d.cgi?scope=all').text

import re
allgenres = re.findall(r'style="color: #.*?>(.*?)<', everynoisetext)

for genre in allgenres:
    print ('insert into MusicGenres values ("{}");'.format(genre))