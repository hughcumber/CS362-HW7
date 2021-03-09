import unittest

class TestFizzbuzz(unittest.TestCase):


    def test_fizzbuzz(self):
        ret_array = fizzbuzz();
        self.assertEqual(ret_array[2], "Fizz");



if __name__ == '__main__':
    unittest.main()
