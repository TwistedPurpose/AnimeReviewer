import sqlite3, DatabaseBuilder, AnimeFetcher

class DBFiller:
    def __init__(self):
        self.__conn = None
        
    def connect(self):
        self.__conn = sqlite3.connect('inorichan.db')
        cursor = self.__conn.cursor()
        return cursor

    def close(self):
        self.__conn.close()

    def commit(self):
        self.__conn.commit()
    
    def addAnimeListToDB(self,animeList):
        cursor = self.connect()
        cursor.executemany('''INSERT OR IGNORE INTO anime VALUES
                (?,?,?,?,?,?,?,?)''',animeList)
        self.commit()
        self.close()
    
    def fillDBWithAnime(self):
        print "I hope DB Senpai notices me!"
        builder = DatabaseBuilder.DBBuilder()
        builder.build()

        fetcher = AnimeFetcher.Fetcher()
        animeList = fetcher.fetchAnime()

        dbAnimeList = []

        for anime in animeList:
                tup = (anime.malId,anime.title,anime.score, anime.animeType,
                       anime.startDate,anime.endDate,anime.episodes,'')
                dbAnimeList.append(tup)

        self.addAnimeListToDB(dbAnimeList)
        
        print "All done!  DB Senpai noticed me!"


filler = DBFiller()
filler.fillDBWithAnime()
