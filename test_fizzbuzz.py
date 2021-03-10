import unittest
import fizzbuzz

class TestFizzbuzzTestCase(unittest.TestCase):


    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz");
        self.assertEqual(fizzbuzz.fizzbuzz(7), 7);
        self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz");
        self.assertEqual(fizzbuzz.fizzbuzz(100), "Buzz");



if __name__ == '__main__':
    unittest.main()
