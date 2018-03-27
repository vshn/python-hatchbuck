import unittest
import sys
sys.path.append('..')

from hatchbuck import Hatchbuck

class TestHatchbuck(unittest.TestCase):

    def setUp(self):
        pass

    def test_search_email(self):
        email = Hatchbuck.search_email(self, 'bashar.said@vshn.ch')
        self.assertEqual(isinstance(email, search_email ))


if __name__ == '__main__':
    unittest.main()