import requests
import xml.etree.ElementTree as ET

class Anime: 
    def __init__(self, malId, title, score, animeType, startDate, endDate, episodes, description):
        self.malId = malId
        self.title = title
        self.score = score
        self.animeType = animeType
        self.startDate = startDate
        self.endDate = endDate
        self.episodes = episodes
        self.description = description

class Fetcher:
        
    def parseAnimeXML(self,xml):
        animeXML = ET.fromstring(xml)
        animeList = []
        for entry in animeXML:
            malId = entry.find('id').text
            title = entry.find('title').text
            score = entry.find('score').text
            animeType = entry.find('type').text
            startDate = entry.find('start_date').text
            endDate = entry.find('end_date').text
            episodes = entry.find('episodes').text
            description = entry.find('synopsis').text
            animeObj = Anime(malId,title,score,animeType,startDate,endDate,episodes,description)
            animeList.append(animeObj)
        return animeList

    def fetchAnime(self):
        fileName = "AnimeTitles.txt"
        url = 'http://myanimelist.net/api/anime/search.xml'
        animeTitleList = []
        animeList = []
        i = 0

        with open(fileName) as file:
            for line in file:
                animeTitleList.append(line)

        for restfulAnimeTitle in animeTitleList:
            requestParameters = { 'q': restfulAnimeTitle.strip() }
            r = requests.get(url,auth=('DatabaseChan','R4pperPhotoElectricTail'), params=requestParameters)
            if (r.status_code == 200):
                animeList.extend(self.parseAnimeXML(r.content))
                i = i + 1
                if (i % 10 == 0):
                    print "Fetched " + str(i) + " records so far."
            else:
                print "Could not fetch " + restfulAnimeTitle.strip()
        return animeList
