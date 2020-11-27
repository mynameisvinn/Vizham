from unittest import TestCase

from Vizham import generate_fingerprint, contains_snippet


class TestMatching(TestCase):

    def test_subsegment_matching(self):
        long_str = [1,1,1,3,4]
        good_short_str = [1,3,4]
        bad_short_str = [1,2,1]

        self.assertTrue(contains_snippet(long_str, good_short_str))
        self.assertFalse(contains_snippet(long_str, bad_short_str))
        