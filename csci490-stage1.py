from Charlotte import Charlotte

import json
import operator
import os


def save_data(stemmed_words, directory, topBottom):
    data = []

    for word in stemmed_words:
        data.append(word[0])

    json_stemmed_words = json.dumps(data, indent=4, sort_keys=True)

    filename = directory.split('/')[3]
    directory_name = directory.split('/')[2]
    filename = 'results/'+ directory_name + '/' + filename + '-' + topBottom + '-200.json'

    with open(filename, 'w+') as file:
        file.write(json_stemmed_words)

def process_html():
    msC = Charlotte()
    filenames = msC.get_all_filenames_from_dir()

    if os.path.exists('./results/master.html') is not True:
        msC.concat_files(filenames, 'results/master.html')

    file_data = msC.process_html_file('results/master.html')
    msC.word_data["summary"] = sorted(msC.word_data["summary"].items(),
                                      key=operator.itemgetter(1))  
    with open('results/master.json', 'w') as outfile:
        outfile.write(json.dumps(msC.word_data["summary"], indent=4))

def write_top_words():
    with open('results/master.json', 'r') as infile:
        words = json.load(infile)
    with open('results/master-top.json', 'w') as outfile:
        outfile.write(json.dumps(words[-200:]))
    with open('results/master-bottom.json', 'w') as outfile:
        outfile.write(json.dumps(words[:200]))

def get_matching_words():
    with open('results/master-train.json', 'r') as infile:
        train_data = json.loads(infile.read())
    with open('results/master-test.json', 'r') as infile:
        test_data = json.loads(infile.read())

    both_words = []

    for test_word in test_data:
        for train_word in train_data:
            if test_word[0] == train_word[0]:
                both_words.append(test_word[0])
                
    with open('results/both-words.json', 'w') as outfile:
        outfile.write(json.dumps(both_words, indent=4) )
if os.path.exists('./results/master.json') is not True:
    process_html()
write_top_words()
get_matching_words()