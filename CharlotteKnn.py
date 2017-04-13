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

    training_data = {}

    def __init__(self):
        super().__init__()
        self.training_data = self.createData("train")
        self.createData("test")


    def euclideanDistance(self, instance1, instance2):
        distance = 0

        for word in instance1:
            if word in instance2:
                distance += pow((instance1[word]['occurrences'] - instance2[word]['occurrences']), 2)
        return math.sqrt(distance)

    # Pre processes the html and creates JSON representations of the HTML file
    # Data type (string): either 'test' or 'train' depending on what type needs to be made
    def createData(self, dataType):
        if os.path.exists('results/' + str(dataType) + '.json') is not True:
            file_data = {}
            target_dir = './assets/projectdata/' + str(dataType) + '/'
            for root, dirs, files in os.walk(target_dir, topdown=False):
                for d in dirs:
                    for f in os.listdir(root + d):
                        file_data[f] = self.process_html_file(root + d + '/' + f)
                        file_data[f]['category'] = d
                if os.path.isdir("results") is not True:
                    os.makedirs('results')
                with open('results/' + str(dataType) + '.json', 'w+') as outfile:
                    outfile.write(json.dumps(file_data, indent=4) )
            return file_data
        else: 
            with open('results/' + str(dataType) + '.json', 'r') as file_data:
                return json.loads(file_data.read())

    # testInstance: one file object that has stop words but not category
    # k: the number of neighbors needed to categorize the testInstance
    def getNeighbors(self, testInstance, k):
        distances = []
        for webpage in self.training_data.keys():
            dist = self.euclideanDistance(testInstance, self.training_data[webpage]["stemmed_words"])
            distances.append((webpage, dist))

        # Sorting the files by distance
        distances.sort(key=operator.itemgetter(1))
        
        neighbors = []
        for x in range(k):
            if(len(distances)):
                neighbors.append(distances.pop())
        return neighbors    
                
    # Takes in the nearest neighbors objects and checks their classification, 
    # returning the classification with the highest number of present
    def getNeighborsVotes(self, neighbors):
        votes = {}
        for neighbor in neighbors:
            classification = self.training_data[neighbor[0]]['category']
            if classification in votes:
                votes[classification] += 1
            else:
                votes[classification] = 1
    
        # Sorting by votes
        s = [(k, votes[k]) for k in sorted(votes, key=votes.get, reverse=True)]
        
        # Returns the classification with the most votes 
        return s[0][0]


        
