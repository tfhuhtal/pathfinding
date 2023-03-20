import unittest
from main import funktio


class TestFunktio(unittest.TestCase):
    """
    Testaa funktio-funktiota
    """
    def test_funktio(self):
        self.assertEqual(funktio(), "Hello world!")
