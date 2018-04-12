import unittest
from src.truthy import returns_true


class Test(unittest.TestCase):
    def test_shouldReturnTrue(self):
        self.assertTrue(returns_true())
