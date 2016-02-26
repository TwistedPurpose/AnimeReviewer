import sqlite3, sys

class DBBuilder:
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

        def clobberAndRebuild(self):
                print "Clobbering DB and rebuilding!  Uguu!"
                cursor = self.connect()
                cursor.execute('''DROP TABLE IF EXISTS anime''')
                cursor.execute('''CREATE TABLE anime
                                (id int primary key,
                                title varchar(50),
                                score int,
                                animeType int,
                                startDate date,
                                endDate date,
                                episodes int,
                                description varchar(500)
                                )''')
                self.commit()
                self.close()
                
        def build(self):
                print "Building a new DB! Nyaa!"
                cursor = self.connect()
                cursor.execute('''CREATE TABLE IF NOT EXISTS anime
                                (id int primary key,
                                title varchar(50),
                                score int,
                                animeType int,
                                startDate date,
                                endDate date,
                                episodes int,
                                description varchar(500)
                                )''')
                self.commit()
                self.close()


