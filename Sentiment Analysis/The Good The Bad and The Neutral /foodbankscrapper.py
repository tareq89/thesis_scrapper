import nltk
import json
import re


def Read(filepath):
	file = open(filepath, 'r')
	text = file.read()
	# print text
	return text

def EncodeJson(jsonString):
	Json = json.loads(jsonString)
	return Json


jsonText = Read("json")

Json = EncodeJson(jsonText)


i = 1
def Process(x):
	i = 1
	mainRsult = ""
	try:
		# print "\n\n\n\n\n\n\n"
		i = i + 1		
		mes =  str(i) + "   :   " + str(x["message"]) + "\n"
		mainRsult  = mainRsult +  "\n\n\n\n\n" + mes + "\n\n"
		# print mes
		tokenized = nltk.word_tokenize(x["message"])
		tagged = nltk.pos_tag(tokenized)
		# print tagged
		# print str(y)
		# chunkGram = r"""Chunk : 
		# 						{<.*>}
		# 						}<RB|NNS>{
		# 						"""
		# chunkParser = nltk.RegexpParser(chunkGram)
		# chunked = chunkParser.parse(tagged)
		# print chunked
		# chunked.draw()

		

		namedEnt = nltk.ne_chunk(tagged, binary=True)
		# mainRsult += str(namedEnt)
		# print namedEnt
		# namedEnt.draw()

		# entities = re.findall(r'NE\s(.*?)/', str(namedEnt))
		entities = re.findall(r'(.*?)/JJ', str(namedEnt))

		print entities

		mainRsult += str(entities)
		fileS = open("result.txt", 'w')
		fileS.write(mainRsult)
		# print mainRsult

	except Exception, e:
		print "Exception in Try  " + str(e)


# for x in Json:
# 	Process(x)

# Process(Json[89])

mainRsult = ""
i = 1
for x in Json:


	try:
		# print "\n\n\n\n\n\n\n"
		i = i + 1		
		mes =  str(i) + "   :   " + str(x["message"]) + "\n"
		mainRsult  = mainRsult +  "\n\n\n\n\n" + mes + "\n\n"
		# print mes
		tokenized = nltk.word_tokenize(x["message"])
		tagged = nltk.pos_tag(tokenized)
		# print tagged
		# print str(y)
		# chunkGram = r"""Chunk : 
		# 						{<.*>}
		# 						}<RB|NNS>{
		# 						"""
		# chunkParser = nltk.RegexpParser(chunkGram)
		# chunked = chunkParser.parse(tagged)
		# print chunked
		# chunked.draw()

		

		namedEnt = nltk.ne_chunk(tagged, binary=True)
		# mainRsult += str(namedEnt)
		# print namedEnt
		# namedEnt.draw()

		# entities = re.findall(r'NE\s(.*?)/', str(namedEnt))
		entities = re.findall(r'(.*?)/JJ', str(namedEnt))

		# print entities

		mainRsult += str(entities)
		
		# print mainRsult

	except Exception, e:
		print "Exception in Try  " + str(e)


# fileS = open("result.txt", 'w')
# fileS.write(mainRsult)
