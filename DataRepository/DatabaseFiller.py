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
        
        def addAnimeListToDB(self,animeList):
                cursor = self.connect()
                cursor.execute('''INSERT INTO anime VALUES
                        (?,?,?,?,?,?,?,?)''',animeList)
                self.close()
        
        def fillDBWithAnime(self):
                print "I hope DB Senpai notices me!"
                builder = DatabaseBuilder.DBBuilder()
                builder.clobberAndRebuild()

                fetcher = AnimeFetcher.Fetcher()
                animeList = fetcher.fetchAnime()

                dbAnimeList = []

                for anime in animeList:
                        dbAnimeList.append((anime.malId,anime.title,anime.score, anime.animeType,
                        anime.startDate,anime.endDate,anime.episodes,''))

                print dbAnimeList[1]
                self.addAnimeListToDB(dbAnimeList)
                
                print "All done!  DB Senpai noticed me!"


filler = DBFiller()
filler.fillDBWithAnime()
