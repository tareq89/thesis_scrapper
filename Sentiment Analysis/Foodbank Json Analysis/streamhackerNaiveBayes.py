import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import json

def Write(filepath, data):
	open(filepath,'w').write(data)

def Read(filepath):
	file = open(filepath, 'r').read()
	return file



def word_feats(words):
    return dict([(word, True) for word in words])

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

# print posids

# negids = ["neg/cv000_29416.txt",
# 	"neg/cv000_29416.txt",
#   	"neg/cv001_19502.txt",
#   "neg/cv002_17424.txt",
#   "neg/cv010_29063.txt"]

# posids = ["pos/cv000_29590.txt",
#  "pos/cv001_18431.txt",
#  "pos/cv002_15918.txt",
#  "pos/cv003_11664.txt"]



# negfeats = []
# posfeats = []

#########################################################################
from os import listdir
from os.path import isfile, join
mypath = "/home/tareq/Desktop/Link to foodbank/Foodbank Json Analysis/data/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

# print onlyfiles

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
			x = nltk.word_tokenize(x["Message"].encode("ascii","ignore"))
			posReview.append(x)

print len(posReview)
# print posReview[0]

 

##############################################################################
for x in allReviews:
	if x["Value"] < 0:
		if x["Message"] != None:
			x = nltk.word_tokenize(x["Message"].encode("ascii","ignore"))
			negReview.append(x)

print len(negReview)
# print negReview[0]
##############################################################################

posfeats = []
negfeats = []
negfeats = [(word_feats(f), 'neg') for f in negReview]
posfeats = [(word_feats(f), 'pos') for f in posReview]
 
open("negfeats.txt",'w').write(json.dumps(negfeats))
open("posfeats.txt",'w').write(json.dumps(posfeats))


# negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
# posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]




negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4

# print movie_reviews.words(fileids=["pos/cv003_11664.txt"])
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]

# print trainfeats[0:10]


testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features(1000)
# print classifier.most_informative_features()

test = [({"This movie sucks but Leonardo was good":True}, 'neg')]
# test = "it was really tasty and awsome..I went to and thought let me try.. got surprised."

# test = [(word_feats(test), 'neg')]

# result = NaiveBayesClassifier.classify(classifier,test)
# print result