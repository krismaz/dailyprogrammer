#Macbeth is totally on the interwebz
import re
from urllib import request
import bs4, time #BeautifulSoup4

phrase = input()

opener = request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')] #Just in case
response = opener.open('http://www.online-literature.com/booksearch.php?id=macbeth&term1=' + phrase.replace(' ', '%20')) #Construct the URL
soupifyAllTheWebz = bs4.BeautifulSoup(response.read()) #Soup parses html, or something
link = soupifyAllTheWebz.find_all('a', text=re.compile('Macbeth - '))[0] #This finds the first search result

print(link.get_text().split('-')[1].split('.')[0][1:]) #Act
print(link.get_text().split('-')[1].split('.')[1][1:]) #Scene

opener = request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')] #Just in case
response = opener.open(link['href']) #Follow the link to the text
soupifyAllTheWebz = bs4.BeautifulSoup(response.read()) #Soup parses html, or something

for p in soupifyAllTheWebz.find_all('p', text=False):
	if phrase in p.text:
		print('Spoken by ' + p.contents[0][:-1] + ':')
		print('\n'.join('    ' + str(c) for c in p.contents[1:] if not str(c) == '<br/>')) #At least finding the entire paragraph is easy