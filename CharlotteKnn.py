import json
import math
import operator
import os

from Charlotte import Charlotte

# Expecting Dicts Like: 
#     "filename"{
#         "words"{
#             "comput": 200
#             ...
#         },
#         "category": "student
#     }


class CharlotteKnn(Charlotte):

    def euclideanDistance(self, instance1, instance2):
        distance = 0

        for word in instance1:
            if word in instance2:
                print(str(pow((instance1[word]['occurrences'] - instance2[word]['occurrences']), 2)))
                distance += pow((instance1[word]['occurrences'] - instance2[word]['occurrences']), 2)
                return math.sqrt(distance)
            else:
                return 0

    def createTrainingData(self):
        if os.path.exists('results/test.json') is not True:
            file_data = {}
            target_dir = './assets/projectdata/test/'
            for root, dirs, files in os.walk(target_dir, topdown=False):
                for d in dirs:
                    for f in os.listdir(root + d):
                        file_data[f] = process_html_file(root + d + '/' + f)
                        file_data[f]['category'] = d
                with open('results/test.json', 'w+') as outfile:
                    outfile.write(json.dumps(file_data, indent=4) )
            return file_data
        else: 
            with open('results/test.json', 'r') as file_data:
                return json.loads(file_data.read())

    # trainingSet: contains all stop words and categories from the training files
    # testInstance: one file object that has stop words but not category
    # k: the number of neighbors needed to categorize the testInstance
    def getNeighbors(self, trainingSet, testInstance, k):
        distances = []

        for webpage in trainingSet.keys():
            dist = self.euclideanDistance(testInstance, trainingSet[webpage]["stemmed_words"])
            distances.append((webpage, dist))

        distances.sort(key=operator.itemgetter(1))
        for webpage in distances:
            print(str(webpage[0]) + ": " + str(webpage[1]))
        neighbors = []
        for x in range(k):
            if(len(distances)):
                neighbors.append(distances.pop())
        return neighbors    
                

