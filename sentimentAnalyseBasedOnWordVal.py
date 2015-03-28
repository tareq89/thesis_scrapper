# -*- coding: utf-8 -*-
from __future__ import division
import json
import nltk



filepath = "weightedWords without repeated.txt"



def Read(filepath):
	file = open(filepath, 'r').read()
	return file

def Write(filepath, data):
	open(filepath,'w').write(data)

def SepareteMsgFromJson():

	foodBankJson = json.loads(Read("foodbank.txt"))
	messageList = []
	for x in foodBankJson:
		messageList.append(x["message"])	
	Write("messageList.txt",json.dumps(messageList))



def TwoDimensionalSentimentAnalysis(Messages):
	wordsWithWeight = open(filepath, 'r').read()
	wordsWithWeight = json.loads(wordsWithWeight)

	PositiveAxis = 0
	NegativeAxis = 0

	sentCounter = 0
	PositiveAxis = 0
	NegativeAxis = 0
	for eachWeightedWord in wordsWithWeight:	
		try:
			tokenizedMessage = nltk.word_tokenize(Messages.encode('utf-8'))
			if eachWeightedWord["word"] in tokenizedMessage:	
				# print eachWeightedWord["word"] + " : " + str(eachWeightedWord["value"]) 				
				if eachWeightedWord["value"]>0:
					PositiveAxis += eachWeightedWord["value"]
					# print "This is Positive - " + eachWeightedWord["word"] +" : "+ str(PositiveAxis)
				elif eachWeightedWord["value"]<0:
					NegativeAxis += eachWeightedWord["value"]
					# print  "This is Negative : " + eachWeightedWord["word"] +" : "+ str(NegativeAxis)
		except Exception, e:
			pass
			# print "Exception : " + str(e)		
	# print "Total PositiveAxis : "+ str(PositiveAxis)
	# print "Total NegativeAxis : "+ str(NegativeAxis)

	result = [PositiveAxis, NegativeAxis]
	return result	



def SymbolTagger(result):
	symbol = ""

	sentCounter = result[0] + result[1]

	try:
		if sentCounter > 0:						
			symbol = "go"
			pass 
		elif sentCounter == 0:												
			symbol = "bo"
		elif sentCounter < 0:																
			symbol = "ro"
		print "_____________________________________________________________________\n\n\n\n"
	except Exception, e:
	 	pass 


	return symbol

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output




# Messages = """We all love the food of Foodrepublic Banani right? I liked it too! 
# But today me and my friends were insulted very badly by a waiter of that place! We were waiting 
# for some friends after our meals! A waiter came and started saying that why weren't we paying the 
# bill and why weren't we leaving? We said that we were waiting for some friends! Then he told us to
# order something ! We said we will order later. Then he insulted us by saying that you guys only ate 
# food of 1600 taka and still sitting here without ordering and if you want to sit here then order something!
# And guys we just finished our food and was drinking our shakes! After this much humiliation we went out to complain
# it to the manager! Luckily the owner was there and he was sorry about it and told that waiter to apologize to us! 
# Though he apologized, it was really humiliating! I went to many restaurants which are way classier than this place but
# never was humiliated in this way! 1600taka! Is it that cheap?"""

# Messages = """Environment: Too good (10/10)
# 				Taste: 1 slice is enough for me ( 9.5/10)
# 				Price : mushroom pizza with pepsi 320tk
# 				Overall worth every penny"""
# Messages = """I ordered food from Sahi Khabar Dabar again today... N O my God!!!! It was even better..... This guys rock at deshi and indian and Sahi food...
# Rate- 9.99999/10 (as i cnt control myself)
# # Behaviori cnt rate their behavior... As their are the best food peoplei ever met....
# Happiness- 1000000000"""


def NormalizeAxis(result):
	X = result[0]
	Y = result[1]

	try:
		# print X
		# print Y

		Y *= -1

		Z = X + Y
		# print Z

		P = 0.00
		Q = 0.00

		P = (X/Z)
		Q = (Y/Z)

		A = P + Q

		# print P
		# print Q
		# print A

		Z = [P,Q]
		return Z
	except Exception, e:
		Z = [X, Y]
		return Z






Messages = open("json2.txt", 'r').read()
Messages = json.loads(Messages)



resultList = []
i = 0
print len(Messages)
for message in Messages:
	try:
		messagePost = message["message"].encode('utf-8')
		# print message
		result =  TwoDimensionalSentimentAnalysis(messagePost)
		result = NormalizeAxis(result)
		message["sentiment"]["pos"] = result[0]
		message["sentiment"]["neg"] = result[1]
		message["sentiment"]["sentiment"] = "checked"

		resultList.append((message))
		i+=1
		print str(len(Messages))+"   ********    "+ str(i) +" : "+ str(result)
	except Exception, e:
		resultListStr = json.dumps(resultList)
		Write("json2WithSentiment.txt", (resultListStr))

resultListStr = json.dumps(resultList)
Write("json2WithSentiment.txt", (resultListStr))	


# result =  TwoDimensionalSentimentAnalysis(Messages)
# print result
# print NormalizeAxis(result)


