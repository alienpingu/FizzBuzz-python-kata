import unittest
import main

class testFizzBuzz(unittest.TestCase):
    def testFizz(self):
        risultato = main.core(3)
        self.assertEqual(risultato,  'Fizz')
    def testBuzz(self):
        risultato = main.core(5)
        self.assertEqual(risultato,  'Buzz')
    def testFizzBuzz(self):
        risultato = main.core(15)
        self.assertEqual(risultato,  'FizzBuzz')
    def testNumber(self):
        risultato = main.core(2)
        self.assertEqual(risultato,  2)