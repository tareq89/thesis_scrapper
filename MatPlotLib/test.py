from pylab import *
import matplotlib.pyplot as plt

def Read(filepath):
	file = open(filepath, 'r').read()
	return file

results = eval(Read("/home/tareq/Documents/Thesis_Scrapper/MatPlotLib/tuples.txt"))


for x in results:
	plt.plot(x[0], x[1], x[2])
# plt.plot([4], [-1], 'go')


# plt.plot([1,2,3,4], [1,2,8,20], 'go')


# plt.plot([1,2,3,4], [1,3,10,30], 'go')
plt.axis([-10, 30, -10, 10])
plt.show()
