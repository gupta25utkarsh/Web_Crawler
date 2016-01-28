import urllib
import urllib2
import sys
import re
from bs4 import BeautifulSoup

processed = []

def searchUrl(url = "http://www.fb.com", depth = 2):
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	if depth == 0 :
		return
	for tag in soup.find_all('a', href=True):
		if ( url + tag['href'] ) not in processed:
			tag['href'] = url + tag['href']
			processed.append(tag['href'])
			searchUrl(tag['href'],depth - 1)

def main():
	if len(sys.argv) < 3:
		print "Give URL and depth"
		sys.exit(-1)
	processed.append(sys.argv[1])
	searchUrl(sys.argv[1],sys.argv[2])
	for a in processed:
		print a

if __name__ == '__main__':
	main()
