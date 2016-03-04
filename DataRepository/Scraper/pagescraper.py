import urllib2
import sys
import re #parse Int out of Text
from bs4 import BeautifulSoup

#Scrapes statistics from MyAnimeList Page
#ratingCount
#duration
#Age Rating

#outfile = open("Statistics.txt",'w')

data = []
ids = {15}

for i in ids:
	mangaurl = 'http://myanimelist.net/manga/'+str(i)
	animeurl = 'http://myanimelist.net/anime/'+str(i)
	
	if (len(sys.argv) > 2 ) and sys.argv[2] == "manga" :
		url = mangaurl
	else:
		url = animeurl

	#print "URL: "+ url
	soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml" )

	ratingCount = 0
	#get RatingCount
	ratingTable = soup('div', {'itemprop': 'aggregateRating'})
	
	for row in ratingTable:
		ref1 = row.find_all('span', {'itemprop':'ratingCount'})
		for x in ref1:
			ratingCount = x.get_text().strip()
	
	#If we are searching an anime page
	#get duration, rating(age), and genre
	duration = ""
	rating = ""
	genre = ""	
	if (url == animeurl):
		table = soup('td', {'class': 'borderClass'})
		for row in table:
			ref1 = row.find_all('div')
			durationflag = False
			for x in ref1:
				text = x.get_text().strip()
				if text.startswith("Duration"):
					array = text.split(" ",1)
					duration = array[1].strip()
				if text.startswith("Rating"):
					array = text.split(" ",1)
					rating = array[1].strip()
				if text.startswith("Genre"):
					array = text.split("\n",1)
					genre = array[1].strip()


	tup = (i, ratingCount.encode("utf-8"), duration.encode("utf-8"), rating.encode("utf-8"), genre.encode("utf-8"))
	
	#If we are searching a manga page, do not return duration and rating
	#tup = (i, ratingCount.encode("utf-8"))
	data.append(tup)
	print tup
