#easy_install BeautifulSoup4
#        easy_install lxml
        
import urllib2
from bs4 import BeautifulSoup



#soup = BeautifulSoup(urllib2.urlopen("http://www.anime-planet.com/manga/all?page=1").read(), "lxml" )

#soup = BeautifulSoup(urllib2.urlopen("https://www.mangaupdates.com/series.html?page=1&perpage=100").read(), "lxml" )

outfile = open("spacecowboyanime.txt",'w')

data = []
pages = {1,2,6}

for i in pages:
	print i
	mangaurl = 'http://myanimelist.net/mangalist/spacecowboy?status='+str(i)+'&tag='
	animeurl = 'http://myanimelist.net/animelist/spacecowboy?status='+str(i)+'&tag='
	url = animeurl
	print url
	soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml" )
	table = soup('div', {'id': 'list_surround'})
	for row in table:
		ref1 = row.find_all('a',{'class':'animetitle'})
		for x in ref1:
			text = x.get_text()
			print text.strip()
			if (len(text) > 0):
				outfile.write(text.strip().encode("UTF-8") + '\n')
outfile.close()