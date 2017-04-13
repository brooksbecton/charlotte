import json
import matplotlib.pyplot as plt

from CharlotteKnn import CharlotteKnn


def main():
    x = []
    y = []
    for i in range(1,466):

        msC = CharlotteKnn()
        test_data = {}

        wordCountThresh = 1

        with open('results/test.json', 'r') as file_data:
            test_data = msC.remove_noisy_words(json.loads(file_data.read()), wordCountThresh)
        with open('results/test.json', 'w') as file_data:
            file_data.write(json.dumps(test_data))
        with open('results/train.json', 'r') as file_data:
            train_data = msC.remove_noisy_words(json.loads(file_data.read()), wordCountThresh)
        with open('results/train.json', 'w') as file_data:
            file_data.write(json.dumps(train_data))
        
        # Typically k = N^(1/2) where N is the number of attributes
        # Attributes being each word found
        k = i

        correctClassification = 0

        # The number of pages processed
        pageCount = 0

        for key in test_data:
            expected_classification = test_data[key]["category"]
            
            # Returns K number of nearest neighbors
            neighbors = msC.getNeighbors(test_data[key]['stemmed_words'], k)
            
            # Gets the classification of the the surrounding K neighbors with the most members present
            classification = msC.getNeighborsVotes(neighbors)

            if classification == expected_classification:
                correctClassification += 1

            pageCount += 1
        x.append(i)
        y.append(correctClassification / pageCount)
        print(str(i) + ", " + str(correctClassification / pageCount))

    with open("results/kValuesGraphData.json", 'w+') as outfile:
        data = {'x': x, 'y':y}
        outfile.write(json.dumps(data))
    plt.plot(x,y)
    plt.xlabel('Value of K')
    plt.ylabel('Accuracy')
    plt.show()


main()