import unittest
import string_helper as sh

class TestStringHelper(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual("tseirPsaduJ", sh.reverse_string("JudasPriest"))


if __name__ == '__main__':
    unittest.main()
