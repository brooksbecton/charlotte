import unittest

from Charlotte import Charlotte


class charlotte_test(unittest.TestCase):

    test_charlotte = Charlotte()

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




unittest.main()
