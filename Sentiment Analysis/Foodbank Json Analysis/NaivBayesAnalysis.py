# -*- coding: utf-8 -*-
from __future__ import division
import json
import nltk
from nltk.probability import FreqDist



# posReview = [
#   "Very good food, very tasty @Eatery\n1st pic Herb Grilled Chicken \n2nd Honey Chilli Chicken\nBoth equally good and flavorsome!!!",
#   "I am looking for a good restaurant near gulshan or banani area for our family get together party. around 40 people. budget 700 per person (including vat and others).need help...",
#   "Best place at dhanmondi to hang out with frnds....plz suggest! !! Except boomers,  star, stage, kook, shimanto square.... TIA!!",
#   "(Photo Collected From Page)\n\nItem : Orange Almond Muffin.\n\nPrice : 40 BDT.\n\nTaste : 9/10.\n\nLast evening I went to my friend's house and he gave me this Orange Almond Muffin to eat. Trust me this is the best muffin I have ever had! This muffin has mouth watering orange flavor with rich almonds. It's from this food shop Fenugreek, they take order by phone. I've checked out there page and they also have some other awesome items.\n\nYou guys can check it out. They are new, but amazing!",
#   "Finally my kinda food at a wedding! (Starter)!They served a cold starter platter (steak cuts, chicken steak n cheese, smoked salmon, lobster and some fresh garden salad! Absolutely amazing! Also served traditional kacchi Biriyani, chicken roast, Khashir gosh and jali kebab. Amazing food. Cold platter was 10/10.Decor was great too. Organized by blitz events!",
#   # "it is way better than i expected!! loved it. had lots of mushroom,chicken, prawn & cheeze. loved d proportion of mushroom. i m glad dat i went there with my friends. environment to joss e & food o onek improve hoise. reasonable price, good food & very good place. r ki lage... :D Cafe Cherry Drops\n4 season pizza- 8.5/10\nchicken wings- 9/10 (according to my friend)\nfried rice was good too.\nwil b going again 2mrrw with family. ^_^"
#   "it was really tasty and awsome..I went to and thought let me try.. got surprised."
# ]

# negReview = [
#   "its a negative review...\nworst servicing >:o chailam roasted burger, dilo normal cheese burger, then bollam ata kno? bole oita to hobena.. ajob to!! to bolbina.. thn uthe jete chailam, bole hobe hobe.. oi burger e may b roasted kore anse 40mins por!! mejaj chorome!! already cold coffee n chocolate milk shake order kore felsilam ty ses na koreo uthte parclam na..\nthis burger nt worth 150tk,, cold coffee 50, chocolate milk shake 90\nworst choclate milk shake.. coffee kono rokom.. \nrating-\ntaste: 1/5\nquantity: 1/5\nservice: 0/10 \nHIGHLY RECOMMENDED NOT TO GO THERE! :/ \n(mejaj ato kharap clo j pic o tulte issa hoynai, akta crop kore dilam)",
#   "The worst steak place in town. Took 2 hours to serve the meal which was either undercooked or overcooked and of course nowhere near good. The chicken bbq had blood near the bone and the steak tasted like shit. Moreover, the steak was as hard as concrete. There wasn't any 'cold' drink. All of the bottled ones were normal or above the average temperature. Crowd control was really poor. The management sucks a big time. And after booking the seats a day ago, they couldn't provide the seats on time. At Entrée Café Lounge",
#   "#WARNING..!!!!\nKFC- king fried chicken. \nI never liked this place nor did i evr went B4.however due to being tired went there to sit. Ordered spicy chicken bbq.\n\nReview- one of the worst place I have evr been to. The chicken was sooo salty tht damaged my tastebuds in 2 bites.french fries were cold inside n full of oil becoz they heated the old ones again. Suddenly small Cockroaches started running around the tray :O\nI was trying to call the waiter to show all this, bt he was terribly picking his nose and using the same hand to put the food in tray.\nCouldn't take it anymore so just took 3pics and left in disgust.",
#   "Food quality - 6/10 \nService - 7/10.\nPrice - 3/10.\n\nHad their promotional dinner offer 999+ tk. Total bill was 2567tk+ with coke n sprite. \nFoods are NOT worth the price at all. \n\nSteaks are not that tasty. \nChocolate brownie is good.\nChicken wings are great. \nMushroom cream soup - its milk and mushroom... Not tasty at all, worst taste !",
#   "worst experience ever at entree cafe lounge: steak is overcooked, chicken is undercooked and they gave a butter knife to have the steak, and also made us wait for an hour for the food. \n\n3/10 food\n4/10 service\n6/10 ambience",
#   "The worst Thai soup I ever had ! Its in fnf bashundhara R/A (0/10) . Cashew nut was too much spicy (4/10) . Apple juice and papaya juice was good (8/10). I won't ever go there >.< And 740/-  tk for all this !"
# ]

def Read(filepath):
	file = open(filepath, 'r').read()
	return file



def LowerCase(list):
	outputList = []
	for x in list:
		outputList.append(x.lower())		
	# print outputList
	return outputList


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


def Common(input1, input2):
	output = []
	for x in input1:
		if x in input2:
			output.append(x)
	return output



def ProbabilityCal(reviewList, testText, trainLenghth):
	tokeNizedList = []
	for x in reviewList:
		try:
			# x = unicode(x, 'utf-8')
			# x = nltk.word_tokenize(x.encode("utf-8"))
			x = nltk.word_tokenize(x)
			tokeNizedList += x
		except Exception, e:
			pass
	print "passed"
	tokeNizedList = LowerCase(tokeNizedList)
	# print len(tokeNizedList)
	# print len(uniq(tokeNizedList))

	frequency = FreqDist(tokeNizedList)
	# print frequency.most_common(50)

	# print tokeNizedList
	testText = nltk.word_tokenize(testText.encode("utf-8").lower())

	print Common(uniq(tokeNizedList), testText)

	Prob = 1.00
	oneMinusProb = 1.00

	for x in Common(uniq(tokeNizedList), testText):
		if x in frequency:		
			feature = (frequency[x]/trainLenghth)
			# print "\n\n"+x
			# print "feature : " + str(feature)
			Prob = Prob * feature
			# print Prob

		notFeature = 1-(frequency[x]/trainLenghth)
		# print x +"  :  1 - notFeature : " + str(notFeature)				
		# print oneMinusProb
		if notFeature==0:
			pass
		else:
			oneMinusProb = oneMinusProb * notFeature
		# print "oneMinusProb = " + str(oneMinusProb) + " * " + str(notFeature)
	TotalProbability = 6/12

	# print oneMinusProb

	result = TotalProbability*Prob #*oneMinusProb
	print str(TotalProbability)+" * "+" * "+str(Prob)+" * "+str(oneMinusProb)
	print "Probability : " + "{0:.20f}".format(result)

##############################################################################


from os import listdir
from os.path import isfile, join
mypath = "/home/tareq/Desktop/Link to foodbank/Foodbank Json Analysis/data/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


allReviews = []
for x in onlyfiles:
	allReviews += json.loads(Read("data/"+x))
print len(allReviews)

# print allReviews[0]
posReview = []
negReview = []
##############################################################################

for x in allReviews:
	if x["Value"] > 0:
		if x["Message"] != None:
			posReview.append(x["Message"].encode("utf-8"))

print len(posReview)

 

##############################################################################
for x in allReviews:
	if x["Value"] < 0:
		if x["Message"] != None:
			negReview.append(x["Message"].encode("utf-8"))

print len(negReview)
 
# print negReview[0]

# test = "Food Republic coffee taste good but burger is worst"
# test = "chicken food is good food and try muffin too"
test = "it was really tasty and awsome..I went to and thought let me try.. got surprised."


ProbabilityCal(posReview, test, len(posReview))
ProbabilityCal(negReview, test, len(negReview))

