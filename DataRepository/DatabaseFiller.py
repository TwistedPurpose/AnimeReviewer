import sqlite3, DatabaseBuilder, AnimeFetcher

class DBFiller:
        
        def addAnime(anime):
                
        
        def fillDBWithAnime(self):
                print "I hope DB Senpai notices me!"
                builder = DatabaseBuilder.DBBuilder()
                builder.clobberAndRebuild()

                fetcher = AnimeFetcher.Fetcher()
                animeList = fetcher.fetchAnime()

                


filler = DBFiller()
filler.fillDBWithAnime()
