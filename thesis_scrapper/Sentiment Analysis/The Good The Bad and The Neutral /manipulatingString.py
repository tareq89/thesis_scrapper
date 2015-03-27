import json
from operator import sub


def Read(filepath):
	file = open(filepath, 'r')
	text = file.read()
	# print text
	return text

 
def Write(data, filepath):
	file = open(filepath, 'w').write(data)


def uniq(input):
  output = []
  outputObjList = []
  outputObjList.append("[")
  for x in input:
    if x['word'] not in output:
      output.append(x['word'])      
      outputObjList.append(x)
  return outputObjList


def FindRepeatedObjects(input):
  output = []
  outputObjList = []
  for x in input:
    if x['word'] not in output:
    	output.append(x['word'])
      	outputObjList.append(x)
  for x in outputObjList:
  	input.remove(x)
  return input


def classifyProperly(input1, input2):
  output = []
  for x in input1:
    for y in input2:
      if x==y:
      	output.append(x)

  return output

def SortingStringList():
	fileText = Read("neutral synonims.txt")
	synonimsList = json.loads(fileText)
	# print synonimsList
	uniqList = uniq(synonimsList)
	Write(json.dumps(uniqList),"neutral synonims.txt")
	

def OnlyOneType(pre1, pre2, pre3):
	pre1 = Read(pre1)
	pre2 = Read(pre2)

	pre1List = json.loads(pre1)
	pre2List = json.loads(pre2)

	commonWords = classifyProperly(pre1List, pre2List)
	Write(json.dumps(commonWords), pre3)

	print commonWords
	return commonWords

	
class WeightedWord(object):
	"""docstring for WeightedWord"""
	def __init__(self, word, value):
		super(WeightedWord, self).__init__()
		self.word = word
		self.value = value
		


def ConvertListToWeightedObject(filepath, val, filepath2):
	fileContent = Read(filepath)
	jsonList = json.loads(fileContent)

	jsonList = uniq(jsonList)
	Json = '['
	for x in jsonList:
		wordObj = WeightedWord(x,val)
		Json += json.dumps(vars(wordObj)) + ','
	Json += ']'
	print Json
	Write(Json,filepath2)


def ConvertListToObject(listObj, filepath):

	jsonList = uniq(listObj)
	Json = '['
	for x in jsonList:		
		Json += json.dumps(x) + ','
	Json += ']'
	# print Json
	Write(Json,filepath)


# filepath = "/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/words/best.txt"
# val = 2
# filepath2 = "/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/words/valbest.txt"

# ConvertListToWeightedObject(filepath,val,filepath2)



words = Read("/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/weightedWords.txt")
wordsWithVal = json.loads(words)

print len(wordsWithVal)
bar = uniq(wordsWithVal)
print len(bar)

filepath = "/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/weightedWords.txt"
filepath2 = "/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/weightedWords2.txt"
filepath3 = "/home/tareq/Documents/Thesis_Scrapper/Do Some Analysis/repeatedWords.txt"


foo = FindRepeatedObjects(wordsWithVal)
print len(foo)
ConvertListToObject(foo, filepath3)
# print foo

 