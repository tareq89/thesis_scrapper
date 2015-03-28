import time
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import datetime
import json
# import beautifulsoup4
from bs4 import BeautifulSoup

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders == [('User-agent', 'Mozilla/5.0')]

def Read(filepath):
	file = open(filepath, 'r')
	text = file.read()
	# print text
	return text

 
def Write(filepath, data):
	file = open(filepath, 'w').write(data)
		

def Download(url):
	localvariable = []
	try:
		page = 'http://thesaurus.com/browse/neutral/'
		
		print "Visiting : "+ url
		sourceCode = urllib2.urlopen(url).read()
		# print "Source Code Downloaded"
		# sourceCode = Read('be.html')
		# print sourceCode
		try:

			soup = BeautifulSoup(sourceCode)			
			title = soup.html.head.title
			# print title.string

			div = soup.html.body
			content = soup.select('.relevancy-list')	
			# print content
			for x in content:
				try:
					word = x.select('.text')
					# print word
					for y in word:
						# print y.text
						# Write(y.text+'\n')
						localvariable.append(y.text)

				except Exception, e:
					pass

			content = soup.select('.syn_of_syns')
			
			for x in content:
				try:
					synWord = x.select('a')
					for y in synWord:
						# print y.text
						# Write(y.text+'\n')
						localvariable.append(y.text)
				except Exception, e:
					print "3rd try catch : " + str(e)

		except Exception, e:
			print "2nd try catch : " + str(e)
	
	except Exception, e:
		print "1st try catch : " + str(e)

	# print localvariable
	return localvariable


def FindLimit(page):
	sourceCode = urllib2.urlopen(page).read()
	# sourceCode = Read('be.html')
	try:
		soup = BeautifulSoup(sourceCode)			
		limit = soup.select('.last a')
		limtiInt = limit[0].text.strip()
		return limtiInt

	except Exception, e:
		print "Limit try catch" + str(e)


def Scrap(word, filepath):
	page = 'http://thesaurus.com/browse/'+word+'/'
	limit = FindLimit(page)
	print "Total Page to be visited : " + limit
	# page = 'http://www.thesaurus.com/browse/neutral/'
	i = 0
	# page = page+str(i)


	globaleVariable = Download(page)
	try:
		for i in xrange(0,int(limit)):
			pass
			i = i + 1		
			temp = Download(page + str(i))
			globaleVariable.append(temp)
	except Exception, e:
		raise e
	print json.dumps(globaleVariable)


	 
	Write(filepath, json.dumps(globaleVariable))
	print "Finished"

filepath = "/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/words/"
Scrap("worst", filepath+"worst.txt")