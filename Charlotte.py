from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from stemming.porter2 import stem


class Charlotte:

    target_words = []
    stop_words = []

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def remove_html_tags(self, raw_html):
        #Removes all html tags and concats all strings
        clean_text = BeautifulSoup(raw_html, "html.parser").stripped_strings

        #Creating list of strings
        for clean_strs in clean_text:
            for clean_str in clean_strs.split():
                self.target_words.append(clean_str)
        return self.target_words

    def remove_stop_words(self, unfiltered_words):
        filtered_words = []

        for word in unfiltered_words:
            if word not in self.stop_words:
                filtered_words.append(word)

        return filtered_words

    def filter_stem_words(self, words):
        stemmed_words = []
        for w in words:
            stemmed_words.append(stem(w))
        return stemmed_words



