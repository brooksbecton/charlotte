from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from stemming.porter2 import stem


class Charlotte:

    #Contains words and there meta data indexed by files there are found in
    word_data = {}
    stop_words = []

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def process_html_file(self, filename):
        html = self.read_file(filename)

        file_word_data = {}

        #Creating place to store word data indexed by filename
        file_word_data = {"words": {}, "stemmed_words": {}}

        html_words = self.remove_stop_words(self.remove_html_tags(html))

        for word in html_words:

            stemmed_word = self.stem_word(word)


            try:
                file_word_data["words"][word]
            except KeyError:
                file_word_data["words"][word] = {"stemmed": stemmed_word}

            try:
                file_word_data["stemmed_words"][stemmed_word]
            except KeyError:
                file_word_data["stemmed_words"][stemmed_word] = {}

            if file_word_data["stemmed_words"][stemmed_word]:
                file_word_data["stemmed_words"][stemmed_word]["occurrences"] += 1
            else:
                file_word_data["stemmed_words"][stemmed_word]["occurrences"] = 1


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

    def stem_words(self, words):
        stemmed_words = []
        for word in words:
            stemmed_words.append(self.stem_word(word))
        return stemmed_words



