import unittest
import sys
sys.path.append('..')

from hatchbuck import Hatchbuck

class TestHatchbuck(unittest.TestCase):

    def setUp(self):
        pass

    def test_instantion(self):
        hatchbuck = Hatchbuck('abc123')
        self.assertTrue(isinstance(hatchbuck, Hatchbuck))

if __name__ == '__main__':
    unittest.main()