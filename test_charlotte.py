import unittest

from Charlotte import Charlotte


class charlotte_test(unittest.TestCase):

    test_charlotte = Charlotte()
    maxDiff = None
    #HTML Removal Tests
    def tearDown(self):
        self.test_charlotte.word_data = {"summary": {}}

    def test_remove_html_single_element(self):
        test_string = "<h1>Hello, World</h1>"
        excpected_result = ["hello,", "world"]
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpected_result)

    def test_remove_html_single_element_with_attr(self):
        test_string = "<a href='//www.reddit.com/r/ProgrammerHumor/'>Hello, World</a>"
        excpected_result = ["hello,", "world"]
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpected_result)
    def test_remove_html_two_element(self):
        test_string = "<a href='www.reddit.com/r/ProgrammerHumor/'>Hello, World</a><p>so funny</p>"
        excpected_result = ["hello,", "world", "so", "funny"]
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpected_result)

    def test_remove_html_empty_element(self):
        test_string = "<p></p>"
        excpected_result = []
        self.assertEqual(self.test_charlotte.remove_html_tags(test_string), excpected_result)

    #Stop Words
    def test_remove_stop_word_the(self):
        test_list = ["the", "dog"]
        excpected_result = ["dog"]
        self.assertEqual(self.test_charlotte.remove_stop_words(test_list), excpected_result)

    def test_remove_stop_words(self):
        test_string = ['me', 'couldn', 'up', 'down', 'because', 'his', 'to', 'both', 'those', 'having', 'into', 'her', 'been', 'here', 'again', 'few', 'he', 'most', 'over', 'haven', 'when', 'than', 'myself', 'yourselves', 'no', 'all', 'the', 'now', 'am', 'under', 'shouldn', 'it', 'isn', 'each', 'can', 'but', 'did', 't', 'these', 'where', 'doesn', 'by', 'is', 'as', 'my', 'and', 'theirs', 'yours', 'so', 'there', 'which', 'if', 'only', 'why', 'had', 'their', 'who', 'does', 'after', 'any', 'we', 'yourself', 'same', 'has', 'ours', 'through', 'i', 'ma', 'until', 'too', 'do', 'its', 'd', 'were', 'a', 'of', 'itself', 'during', 'wouldn', 'them', 'further', 'hadn', 'aren', 'very', 'not', 'while', 'an', 'for', 'your', 'or', 'from', 'own', 'weren', 'themselves', 'what', 'y', 'didn', 'against', 'above', 'more', 'needn', 've', 'o', 'himself', 'ourselves', 'below', 'on', 'ain', 'will', 'about', 'once', 'such', 'doing', 'are', 'our', 'herself', 'm', 'out', 'hasn', 'hers', 'be', 'being', 'have', 'they', 'mightn', 'some', 'at', 'him', 'just', 'should', 'between', 'this', 'was', 'll', 'shan', 'whom', 'wasn', 'you', 'off', 'in', 's', 'then', 'don', 'nor', 're', 'how', 'she', 'other', 'that', 'won', 'with', 'mustn', 'before']
        excpected_result = []
        self.assertEqual(self.test_charlotte.remove_stop_words(test_string), excpected_result)

    def test_remove_stop_words_none(self):
        test_list = ["cat", "dog", "parrot", "dinosaur"]
        excpected_result = ["cat", "dog", "parrot", "dinosaur"]
        self.assertEqual(self.test_charlotte.remove_stop_words(test_list), excpected_result)

    def test_remove_stop_words_no_words(self):
        test_list = []
        excpected_result = []
        self.assertEqual(self.test_charlotte.remove_stop_words(test_list), excpected_result)

    def test_stem_word(self):
        test_word = ["computer"]
        expected_result = ["comput"]
        self.assertEqual(self.test_charlotte.stem_words(test_word), expected_result)

    def test_stem_word_two(self):
        test_word = ["computer", "functionality"]
        expected_result = ["comput", "function"]
        self.assertEqual(self.test_charlotte.stem_words(test_word), expected_result)

    def test_process_html_file_basic(self):
        test_file = "assets/tests/test_process_html_file_basic.html"
        expected_result = {
            'words':{
                'sun':{
                    'stemmed': 'sun'
                },
                'shines':{
                    'stemmed': 'shine'
                },
                'bright':{
                    'stemmed': 'bright'
                },
                'today':{
                    'stemmed': 'today'
                }
            },
            'stemmed_words': {
                'sun':{
                    'occurrences': 1
                },
                'shine':{
                    'occurrences': 1
                },
                'bright':{
                    'occurrences': 1
                },
                'today':{
                    'occurrences': 1
                }
            }
        }
        self.assertEqual(self.test_charlotte.process_html_file(test_file), expected_result)

    def test_process_html_files_basic(self):
        test_files = ["assets/tests/test_process_html_file_basic.html"]
        expected_result = {
            'assets/tests/test_process_html_file_basic.html': {
                'words':{
                    'sun':{
                        'stemmed': 'sun'
                    },
                    'shines':{
                        'stemmed': 'shine'
                    },
                    'bright':{
                        'stemmed': 'bright'
                    },
                    'today':{
                        'stemmed': 'today'
                    }
                },
                'stemmed_words': {
                    'sun':{
                        'occurrences': 1
                    },
                    'shine':{
                        'occurrences': 1
                    },
                    'bright':{
                        'occurrences': 1
                    },
                    'today':{
                        'occurrences': 1
                    }
                }
            }
        }

    def test_process_html_files_basic_multi_word(self):
        test_files = ["assets/tests/test_process_html_file_basic_multi_word.html"]
        expected_result = {
            'assets/tests/test_process_html_file_basic_multi_word.html': {
                'words':{
                    'sun':{
                        'stemmed': 'sun'
                    },
                    'shines':{
                        'stemmed': 'shine'
                    },
                    'bright':{
                        'stemmed': 'bright'
                    },
                    'today':{
                        'stemmed': 'today'
                    }
                },
                'stemmed_words': {
                    'sun':{
                        'occurrences': 2
                    },
                    'shine':{
                        'occurrences': 2
                    },
                    'bright':{
                        'occurrences': 2
                    },
                    'today':{
                        'occurrences': 2
                    }
                }
            }
        }

        self.test_charlotte.process_html_files(test_files)

        self.assertEqual(self.test_charlotte.word_data, expected_result)

unittest.main()
