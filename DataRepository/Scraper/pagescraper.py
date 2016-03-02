import urllib2
import re #parse Int out of Text
from bs4 import BeautifulSoup

#Scrapes statistics from MyAnimeList Page
#ratingCount
#duration
#Rating()

#outfile = open("Statistics.txt",'w')

data = []
ids = {15}

for i in ids:
	#print "id "+ str(i)
	mangaurl = 'http://myanimelist.net/manga/'+str(i)
	animeurl = 'http://myanimelist.net/anime/'+str(i)
	url = animeurl
	#print "URL: "+ url
	soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml" )
	#get RatingCount
	ratingTable = soup('div', {'itemprop': 'aggregateRating'})
	#print table
	ratingCount = 0
	for row in ratingTable:
		ref1 = row.find_all('span', {'itemprop':'ratingCount'})
		for x in ref1:
			ratingCount = x.get_text().strip()
#			if (len(text) > 0):
#				outfile.write(text.strip().encode("UTF-8") + '\n')
	#get duration
	duration = ""
	rating = ""
	if (url == animeurl):
		table = soup('td', {'class': 'borderClass'})
		for row in table:
			ref1 = row.find_all('div')
			durationflag = False
			for x in ref1:
				text = x.get_text().strip()
				if text.startswith("Dur"):
					array = text.split(" ",1)
					duration = array[1].strip()
				if text.startswith("Rating"):
					array = text.split(" ",1)
					rating = array[1].strip()
	#			if (len(text) > 0):
	#				outfile.write(text.strip().encode("UTF-8") + '\n')
	tup = (i, ratingCount.encode("utf-8"), duration.encode("utf-8"), rating.encode("utf-8"))
	data.append(tup)
	print tup
#outfile.close()
