from unittest import TestCase
import second


class TestPrime (TestCase):
    def test_print_next_prime(self):
        self.assertEqual(second.factor(6), 720)
