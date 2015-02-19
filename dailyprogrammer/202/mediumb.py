#Everything is online nowadays, so why compute easter dates locally?
from urllib import request
import bs4, time #BeautifulSoup4 

def easter(year):
	opener = request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')] #Apparently the website prefers webbrowsers, intriguing, but fear not!
	response = opener.open('http://www.wheniseastersunday.com/year/' + str(year) + '/') #Construct the URL
	soupifyAllTheWebz = bs4.BeautifulSoup(response.read()) #Soup parses html, or something
	return soupifyAllTheWebz.select('.easterdate')[0].get_text() #Neato, they tagged it and everything!

for date in map(easter, range(2015, 2026)):
	print(date)
	time.sleep(1) #Don't actually spam the server