from Charlotte import Charlotte

import json
import operator
import os

msC = Charlotte()

DIRECTORIES = ['assets/projectdata/test/course/', 'assets/projectdata/test/faculty/', 'assets/projectdata/test/student/']
# DIRECTORIES = ['assets/projectdata/test/student/']

i = 0

for directory in DIRECTORIES:
    FILENAMES = msC.get_all_filenames_from_dir(directory, '.html')

    msC.process_html_files(FILENAMES)

    msC.word_data["summary"] = sorted(msC.word_data["summary"].items(), key=operator.itemgetter(1))
    
    DATA = msC.word_data["summary"][:200]

    JSON_DATA = json.dumps(DATA, indent=4, sort_keys=True)
    if not os.path.exists('results'):
        os.makedirs('results')

    filename = directory.split('/')[3]
    filename = 'results/' + filename + '-top-200.json'
    
    with open(filename, 'w') as f:
        f.write(JSON_DATA)

    msC.word_data["summary"].reverse()

    DATA = msC.word_data["summary"][:200]

    JSON_DATA = json.dumps(DATA, indent=4, sort_keys=True)

    filename = directory.split('/')[3]
    filename = 'results/' + filename + '-bottom-200.json'

    with open(filename, 'w') as f:
        f.write(JSON_DATA)

    msC.word_data = {
        "summary": {}
    }


    i += 1
        