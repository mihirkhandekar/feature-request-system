import unittest

from service.ml.similarity_checker import get_difference_score



class SimilarityCheckerTest(unittest.TestCase):
    def test_get_difference_score(self):
        sim1 = get_difference_score('Hello world', 'Hello earth')
        sim2 = get_difference_score('Hello world', 'What is your name')

        assert sim1 > sim2
