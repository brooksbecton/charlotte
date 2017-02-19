from Charlotte import Charlotte

import json
import operator
import os

def process_html():
    msC = Charlotte()

    DIRECTORIES = ['assets/projectdata/train/student/',
                   'assets/projectdata/train/course/',
                   'assets/projectdata/train/faculty/',
                   'assets/projectdata/test/student/',
                   'assets/projectdata/test/course/',
                   'assets/projectdata/test/faculty/']

    for directory in DIRECTORIES:
        FILENAMES = msC.get_all_filenames_from_dir(directory, '')

        msC.process_html_files(FILENAMES)

        #Sorting stemmed words by weight into a list
        msC.word_data["summary"] = sorted(msC.word_data["summary"].items(),
                                          key=operator.itemgetter(1))

        save_data(msC.word_data["summary"][:200], directory, "bottom")
        msC.word_data["summary"].reverse()
        save_data(msC.word_data["summary"][:200], directory, "top")

        msC.word_data = {
            "summary": {}
        }

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



process_html()