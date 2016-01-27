import urllib
import urllib2
import sys
import re
from bs4 import BeautifulSoup

processed = []

def searchUrl(url = "http://www.google.co.in", depth = 1):
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	if depth == 0 :
		return
	for tag in soup.find_all('a', href=True):
		if tag['href'] not in processed:
			tag['href'] = url + tag['href']
			processed.append(tag['href'])

def main():
	if len(sys.argv) < 2:
		print "Give URL"
		sys.exit(-1)
	processed.append(sys.argv[1])
	searchUrl(sys.argv[1])
	for a in processed:
		print a

if __name__ == '__main__':
	main()