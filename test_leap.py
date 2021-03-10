import unittest
import leap

class TestLeapTestCase(unittest.TestCase):


    def test_leap(self):
        self.assertEqual(leap.leap(2000), "Leap year!");
        self.assertEqual(leap.leap(7), "Not a leap year");
        self.assertEqual(leap.leap(2004),  "Leap year!");
        self.assertEqual(leap.leap(10007), "Not a leap year");



if __name__ == '__main__':
    unittest.main()
