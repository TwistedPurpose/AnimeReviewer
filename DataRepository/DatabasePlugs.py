import sqlite3, AnimeFetcher

class DatabasePlugs:
    def __init__(self):
        self.__conn = None
        
    def connect(self):
        self.__conn = sqlite3.connect('inorichan.db')
        cursor = self.__conn.cursor()
        return cursor

    def close(self):
        self.__conn.close()

    def getAllAnime(self):
        animeList = []
        c = self.connect()
        c.execute('''SELECT id, title, score, animeType, startDate, endDate, episodes, description,
         ratingCount, duration, ageRating from anime''')
        for row in c:
            print row
            anime = AnimeFetcher.Anime(row[0],row[1],row[2],row[3],row[4],row[5],
                row[6],row[7],row[8],row[9],row[10])
            animeList.append(anime)
        self.close()
        return animeList