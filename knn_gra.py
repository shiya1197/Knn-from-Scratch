
import csv
import random
import math
import operator
#import matplotlib.pyplot as G

def loadDataset(filename,divider):
    training=[]
    testing=[]
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in range(len(dataset)-1):
            for j in range(4):
                dataset[i][j] = float(dataset[i][j])
            if random.random() < divider:
                training.append(dataset[i])
            else:
                testing.append(dataset[i])
    return training,testing


def Distance(d1, d2, length):
	d = 0
	for i in range(length):
		d += pow((d1[i] - d2[i]), 2)
	return math.sqrt(d)

def nearestNeighbors(training, point, k):
    distances = []
    length = len(point)-1
    for i in range(len(training)):
        distance1 = Distance(point, training[i], length)
        distances.append((training[i], distance1))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def Accuracy(testing, predictions):
    correct = 0
    for i in range(len(testing)):
        if testing[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testing))) * 100.0
	
def main():
    divider = float(raw_input("enter the dividing norm eg 0.60 for 60% : "))
    training,testing = loadDataset('iris_dataset.csv', divider)
    predictions=[]
    k = int(raw_input("enter the value of k : "))
    #klist=[]
    #acu=[]
    for i in range(len(testing)):
        n = nearestNeighbors(training, testing[i], k)
        result = getResponse(n)
        predictions.append(result)
        #print('> predicted=' + repr(result) + ', actual=' + repr(testing[i][-1]))
    accuracy = Accuracy(testing, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    f = open("test1.txt","a+")
    f.write("%f %d\n" % (accuracy,k))
    #klist.append(k)
    #acu.append(accuracy)
    #print klist
    #f.write("")
    f.close()

'''
    G.plot(klist,acu)
    G.xlabel('variation of K')
    G.ylabel('accuracy')
    G.show()

    '''
main()
