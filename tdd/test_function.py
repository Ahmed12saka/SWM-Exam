"""system model"""
import unittest
from function import my_function


class TestSquareRootOfNumber(unittest.TestCase):
    """math.sqrt"""

    def test_valid_input(self):
        """sqrt root test"""
        sqrt = 36
        root = 6
        self.assertEqual(my_function(sqrt), root)

    def test_empty_input(self):
        """ "testing empty"""
        with self.assertRaises(TypeError):
            self.assertEqual(my_function(None), True)

    def test_invalid_input(self):
        """tes float"""
        input = 2.1
        with self.assertRaises(TypeError):
            self.assertEqual(my_function(input), True)


if __name__ == "__main__":
    unittest.main()
