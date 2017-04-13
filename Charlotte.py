import glob
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from stemming.porter2 import stem


class Charlotte:

    #Contains words and there meta data indexed by files there are found in
    word_data = {
        "summary": {}
    }
    stop_words = []


    def __init__(self):
        self.stop_words = self.gen_stop_words() 
    def concat_files(self, filenames, output_file):
        with open(output_file, 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)


    def gen_stop_words(self):
        stop_words = set(stopwords.words('english'))
        stop_words.add("")
        stop_words.add("mimeversion")
        stop_words.add("contentlength")
        stop_words.add("contenttype")
        stop_words.add("gmt")
        stop_words.add("lastmodified")
        stop_words.add("texthtml")
        stop_words.add("cern")
        stop_words.add("monday")
        stop_words.add("tuesday")
        stop_words.add("wednesday")
        stop_words.add("thursday")
        stop_words.add("friday")
        stop_words.add("saturday")
        stop_words.add("sunday")
        stop_words.add("nov")
        stop_words.add("dec")
        return stop_words

    def get_all_filenames_from_dir(self):
        filenames = []
        for filename in glob.iglob('assets/projectdata/test/**/http*', recursive=True):
            filenames.append(filename)
        return filenames


    def process_html_file(self, filename):
        html = self.read_file(filename)

        file_word_data = {}

        #Creating place to store word data indexed by filename
        file_word_data = {"words": {}, "stemmed_words": {}}

        html_words = self.remove_stop_words(self.remove_html_tags(html))

        for word in html_words:

            stemmed_word = self.stem_word(word)

            #Initing a new words structures
            if word not in file_word_data["words"].keys():
                file_word_data["words"][word] = {"stemmed": stemmed_word}

            if stemmed_word not in file_word_data["stemmed_words"].keys():
                file_word_data["stemmed_words"][stemmed_word] = {}
                self.word_data["summary"][stemmed_word] = 0


            #Checking to see if a stemmed word already exists
            if file_word_data["stemmed_words"][stemmed_word]:
                file_word_data["stemmed_words"][stemmed_word]["occurrences"] += 1
                self.word_data["summary"][stemmed_word] += 1
            else:
                file_word_data["stemmed_words"][stemmed_word]["occurrences"] = 1
                self.word_data["summary"][stemmed_word] = 1

        return file_word_data

    def process_html_files(self, filenames):
        for filename in filenames:
            file_word_data = self.process_html_file(filename)
            self.word_data[filename] = self.remove_noisey_words(file_word_data, 5)

    def remove_noisy_words(self, word_data, wordCountThreshhold):
        for filename in word_data:
            wordsToDel = []
            words = word_data[filename]["stemmed_words"]
            for word in words:
                occurrences = words[word]["occurrences"]
                if occurrences < wordCountThreshhold:
                    wordsToDel.append(word)
            for word in wordsToDel:
                del words[word]

        return word_data

    def remove_html_tags(self, html):
        #Removes all html tags and concats all strings
        clean_text = BeautifulSoup(html, "html.parser").stripped_strings

        words = []

        #Creating list of strings from one long string
        for strs in clean_text:
            for clean_str in strs.split():
                words.append(clean_str.lower())
        return words

    def read_file(self, filename):
        with open(filename) as file:
            return file.read()

    def remove_stop_words(self, unfiltered_words):
        filtered_words = []
        for word in unfiltered_words:
            word  = ''.join(e for e in word if e.isalpha())
            if word not in self.stop_words:
                filtered_words.append(word)

        return filtered_words

    def stem_word(self, word):
        return stem(word)

    def stem_words(self, words):
        stemmed_words = []
        for word in words:
            stemmed_word = self.stem_word(word)
            if stemmed_word.isdigit() == False:
                stemmed_words.append(stemmed_word)
        return stemmed_words



