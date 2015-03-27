import json
import re

regexList = [r'(\d/\d.)',r'(b.?r.?g.?r)', r'([a-z]+( |-|:)(| )(|.)\d?/\d.)']

def Read(filepath):
	text = open(filepath, 'r').read()
	return text;

def RatingDetector():
	jsonString = Read("foodbank.txt")

	foodbankAllPost = json.loads(jsonString)


	posts = []
	i = 0
	j = 0
	for x in foodbankAllPost:
		try:		
			# print "\n\n\n\n\n\n\n\n\n"
			i+=1
			post = (x['message'].encode('utf-8'))
			post = post.replace("\n", "")
			post = post.replace("\t", "")
			post = re.sub(' +',' ', post)
			post = post.lower()
			# print str(i)+") : "+ post

			
			matched = re.findall(regexList[2], post)
			
			if matched[0][0]!=None:
				j+=1
				y = matched[0][0]
				y = re.sub(r':|-',' ',y)
				y = re.sub(' +',' ', y)

			print str(j)+ "  :  "+ y
			# print "Values : \n"
			# print y
		except Exception, e:
			pass
