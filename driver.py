import json

from CharlotteKnn import CharlotteKnn


def main():
    msC = CharlotteKnn()

    test_data = {}

    with open('results/test.json', 'r') as file_data:
        test_data = json.loads(file_data.read())

    predictions=[]

    # Typically k = N^(1/2) where N is the number of attributes
    # Attributes being each word found
    k = 200

    correctClassification = 0

    # The number of pages processed
    pageCount = 0

    for key in test_data:
        expected_classification = test_data[key]["category"]
        # Returns K number of nearest neighbors
        neighbors = msC.getNeighbors(test_data[key]['stemmed_words'], k)
        
        # Gets the classification of the the surrounding neighbors with the most members present
        classification = msC.getNeighborsVotes(neighbors)

        if classification == expected_classification:
            correctClassification += 1

        pageCount += 1

    print("Accuracy:  " + str(correctClassification / pageCount))

        


main()