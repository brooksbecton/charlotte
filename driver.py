import json
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


msC = Charlotte()

file_data = {}

def createTrainingSet():
    target_dir = './assets/projectdata/test/'
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for d in dirs:
            for f in os.listdir(root + d):
                file_data[f] = msC.process_html_file(root + d + '/' + f)
                file_data[f]['category'] = d
        with open('results/test.json', 'w+') as outfile:
            outfile.write(json.dumps(file_data, indent=4) )
        print(len(file_data.keys()))

            
createTrainingSet()