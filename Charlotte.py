from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from stemming.porter2 import stem


class Charlotte:

    word_data = {}
    stop_words = []

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def process_html_file(self, filename):
        html = self.read_file(filename)

        file_word_data = {}

        #Creating place to store word data indexed by filename
        file_word_data = {"words": {}}

        html_words = self.remove_stop_words(self.remove_html_tags(html))

        for word in html_words:
            file_word_data['words'][word] = {"stemmed": self.stem_word(word)}

        return file_word_data

    def process_html_files(self, filenames):
        for filename in filenames:
            file_word_data = self.process_html_file(filename)
            self.word_data[filename] = file_word_data

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
            if word not in self.stop_words:
                filtered_words.append(word)

        return filtered_words

    def stem_word(self, word):
        return stem(word)

    def filter_stem_words(self, words):
        stemmed_words = []
        for word in words:
            stemmed_words.append(self.stem_word(word))
        return stemmed_words



