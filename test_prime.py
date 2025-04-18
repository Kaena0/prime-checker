# test_prime.py

import unittest
from prime import is_prime

class TestIsPrime(unittest.TestCase):

    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))

    def test_non_primes(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))

if __name__ == '__main__':
    unittest.main()
