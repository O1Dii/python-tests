import unittest
from unittest.mock import patch

from calc import Calc


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add_int(self):
        result = self.calc.add(10, 15)
        self.assertEqual(result, 25)

    def test_add_float(self):
        result = self.calc.add(10.1, 15.2)
        self.assertEqual(round(result, 1), 25.3)

    def test_add_str(self):
        result = self.calc.add('aaa', 'bbb')
        self.assertEqual(result, 'aaabbb')

    def test_add_int_str(self):
        with self.assertRaises(TypeError):
            self.calc.add(1, 'aa')


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_sub_int(self):
        result = self.calc.subtract(10, 15)
        self.assertEqual(result, -5)

    def test_sub_float(self):
        result = self.calc.subtract(15.1, 10.2)
        self.assertEqual(round(result, 1), 4.9)

    def test_sub_str(self):
        with self.assertRaises(TypeError):
            self.calc.subtract('aaa', 'bbb')

    def test_sub_int_str(self):
        with self.assertRaises(TypeError):
            self.calc.subtract(1, 'aa')


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_multiply_int(self):
        result = self.calc.multiply(10, 15)
        self.assertEqual(result, 150)

    def test_multiply_float(self):
        result = self.calc.multiply(15.1, 10.2)
        self.assertEqual(round(result, 2), 154.02)

    def test_multiply_str(self):
        with self.assertRaises(TypeError):
            self.calc.multiply('aaa', 'bbb')

    def test_multiply_int_str(self):
        result = self.calc.multiply(2, 'aa')
        self.assertEqual(result, 'aaaa')


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_divide_int(self):
        result = self.calc.divide(20, 2)
        self.assertEqual(result, 10)

    def test_divide_float(self):
        result = self.calc.divide(20.2, 10.1)
        self.assertEqual(round(result), 2)

    def test_divide_str(self):
        with self.assertRaises(ValueError):
            self.calc.divide('aaa', 'bbb')

    def test_divide_float_str(self):
        with self.assertRaises(TypeError):
            self.calc.divide(1.1, 'aa')

    def test_divide_int_str(self):
        with self.assertRaises(TypeError):
            self.calc.divide(2, 'aa')


class TestRandom(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add_called(self):
        with patch('random.randint', return_value=1):
            result = self.calc.random_operation(20, 2)
        self.assertEqual(result, 22)

    def test_sub_called(self):
        with patch('random.randint', return_value=2):
            result = self.calc.random_operation(20, 10)
        self.assertEqual(result, 10)

    def test_multiply_called(self):
        with patch('random.randint', return_value=3):
            result = self.calc.random_operation(20, 10)

        self.assertEqual(result, 200)

    def test_divide_called(self):
        with patch('random.randint', return_value=4):
            result = self.calc.random_operation(20, 10)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
