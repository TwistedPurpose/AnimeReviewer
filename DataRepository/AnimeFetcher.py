import requests

url = 'http://myanimelist.net/api/anime/search.xml?q=full+metal'

r = requests.get(url,auth=('',''))

print r.content
