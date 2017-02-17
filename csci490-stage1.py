from Charlotte import Charlotte

import os
import json

msC = Charlotte()

DIRECTORIES = ['assets/projectdata/test/course/', 'assets/projectdata/test/faculty/', 'assets/projectdata/test/student/']
# DIRECTORIES = ['assets/projectdata/test/student/']

i = 0

for directory in DIRECTORIES:
    FILENAMES = msC.get_all_filenames_from_dir(directory, '.html')

    msC.process_html_files(FILENAMES)

    DATA = msC.word_data

    JSON_DATA = json.dumps(DATA, indent=4, sort_keys=True)
    if not os.path.exists('results'):
        os.makedirs('results')
    filename = 'results/results-' + str(i) + ' .json'

    with open(filename, 'w') as f:
        f.write(JSON_DATA)

    msC.word_data = {
        "summary": {}
    }

    i += 1
        