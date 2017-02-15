import unittest

from Charlotte import Charlotte


class charlotte_test(unittest.TestCase):

    test_charlotte = Charlotte()

    #HTML Removal Tests
    def tearDown(self):
        self.test_charlotte.target_words = []

    def test_remove_html_single_element(self):
        test_string = "<h1>Hello, World</h1>"
        excpectied_result = ["Hello,", "World"]
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpectied_result)

    def test_remove_html_single_element_with_attr(self):
        test_string = "<a href='//www.reddit.com/r/ProgrammerHumor/'>Hello, World</a>"
        excpectied_result = ["Hello,", "World"]
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpectied_result)
    def test_remove_html_two_element(self):
        test_string = "<a href='www.reddit.com/r/ProgrammerHumor/'>Hello, World</a><p>so funny</p>"
        excpectied_result = ["Hello,", "World", "so", "funny"]
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpectied_result)

    def test_remove_html_empty_element(self):
        test_string = "<p></p>"
        excpectied_result = []
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpectied_result)

    def test_remove_stop_word_the(self):
        test_list = ["the", "dog"]
        excpectied_result = ["dog"]
        self.assertEqual(self.test_charlotte.remove_stop_words(test_list), excpectied_result)

    def test_remove_stop_words(self):
        test_string = ['me', 'couldn', 'up', 'down', 'because', 'his', 'to', 'both', 'those', 'having', 'into', 'her', 'been', 'here', 'again', 'few', 'he', 'most', 'over', 'haven', 'when', 'than', 'myself', 'yourselves', 'no', 'all', 'the', 'now', 'am', 'under', 'shouldn', 'it', 'isn', 'each', 'can', 'but', 'did', 't', 'these', 'where', 'doesn', 'by', 'is', 'as', 'my', 'and', 'theirs', 'yours', 'so', 'there', 'which', 'if', 'only', 'why', 'had', 'their', 'who', 'does', 'after', 'any', 'we', 'yourself', 'same', 'has', 'ours', 'through', 'i', 'ma', 'until', 'too', 'do', 'its', 'd', 'were', 'a', 'of', 'itself', 'during', 'wouldn', 'them', 'further', 'hadn', 'aren', 'very', 'not', 'while', 'an', 'for', 'your', 'or', 'from', 'own', 'weren', 'themselves', 'what', 'y', 'didn', 'against', 'above', 'more', 'needn', 've', 'o', 'himself', 'ourselves', 'below', 'on', 'ain', 'will', 'about', 'once', 'such', 'doing', 'are', 'our', 'herself', 'm', 'out', 'hasn', 'hers', 'be', 'being', 'have', 'they', 'mightn', 'some', 'at', 'him', 'just', 'should', 'between', 'this', 'was', 'll', 'shan', 'whom', 'wasn', 'you', 'off', 'in', 's', 'then', 'don', 'nor', 're', 'how', 'she', 'other', 'that', 'won', 'with', 'mustn', 'before']
        excpectied_result = []
        self.assertEqual(self.test_charlotte.remove_stop_words(test_string), excpectied_result)

    def test_remove_stop_words_none(self):
        test_string = ["cat", "dog", "parrot", "dinosaur"]
        excpectied_result = ["cat", "dog", "parrot", "dinosaur"]
        self.assertEqual(self.test_charlotte.remove_stop_words(test_string), excpectied_result)

    def test_remove_stop_words_no_words(self):
        test_string = []
        excpectied_result = []
        self.assertEqual(self.test_charlotte.remove_stop_words(test_string), excpectied_result)


unittest.main()
