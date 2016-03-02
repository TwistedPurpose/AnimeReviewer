import urllib2
from bs4 import BeautifulSoup

#Scrapes statistics from MyAnimeList Page

#outfile = open("Statistics.txt",'w')

data = []
ids = {15}

for i in ids:
	print i
	mangaurl = 'http://myanimelist.net/manga/'+str(i)
	animeurl = 'http://myanimelist.net/anime/'+str(i)
	url = animeurl
	print url
	soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml" )
	ratingTable = soup('div', {'itemprop': 'aggregateRating'})
	#print table
	for row in ratingTable:
		ref1 = row.find_all('span', {'itemprop':'ratingCount'})
		for x in ref1:
			ratingCount = x.get_text()
			print ratingCount.strip()
#			if (len(text) > 0):
#				outfile.write(text.strip().encode("UTF-8") + '\n')
#outfile.close()