from bs4 import BeautifulSoup


class Charlotte:

    target_words = []

    def remove_html_tags(self, raw_html):
        clean_text = BeautifulSoup(raw_html, "html.parser").stripped_strings
        for clean_strs in clean_text:
            for clean_str in clean_strs.split():
                self.target_words.append(clean_str)
        return self.target_words

    def remove_stop_words(self):
        print("remove_stop_words")

    def get_stem_words(self):
        print("get_stem_words")

