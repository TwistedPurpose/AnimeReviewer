#easy_install BeautifulSoup4
#        easy_install lxml
        
import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://myanimelist.net/mangalist/spacecowboy?status=1&tag=').read(), "lxml" )


#soup = BeautifulSoup(urllib2.urlopen("http://www.anime-planet.com/manga/all?page=1").read(), "lxml" )

#soup = BeautifulSoup(urllib2.urlopen("https://www.mangaupdates.com/series.html?page=1&perpage=100").read(), "lxml" )

table = soup('div', {'id': 'list_surround'})



for row in table:
    row.find_all('a',{'class':'animetitle'})
    #print row.find('tr', {'class', 'text pad col1'})
    #print row.find_all('td', {'class', 'text pad col1'})
#for row in soup('table'):
  #tds = row('td')
  #print tds[0].string, tds[1].string

