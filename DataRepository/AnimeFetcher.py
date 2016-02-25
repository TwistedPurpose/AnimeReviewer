import requests

fileName = "AnimeTitles.txt"

animeList = []

with open(fileName) as file:
    for line in file:
            animeList.append(line)

restfulAnimeTitle = animeList[3].strip()

requestParameters = { 'q': restfulAnimeTitle }

print restfulAnimeTitle

url = 'http://myanimelist.net/api/anime/search.xml'
r = requests.get(url,auth=('DatabaseChan','R4pperPhotoElectricTail'), params=requestParameters)

print r.url
print r
print r.content
