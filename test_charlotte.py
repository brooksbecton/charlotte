import unittest

from Charlotte import Charlotte


class charlotte_test(unittest.TestCase):

    test_charlotte = Charlotte()

    def test_remove_html_single_element(self):
        test_string = "<h1>Hello, World</h1>"
        excpectied_result = "Hello, World"
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpectied_result)

unittest.main()
