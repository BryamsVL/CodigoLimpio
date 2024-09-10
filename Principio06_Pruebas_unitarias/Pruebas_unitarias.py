import unittest

class Calculadora:
    def sumar(self, a, b):
        return a + b

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        calc = Calculadora()
        self.assertEqual(calc.sumar(2, 3), 5)
        self.assertEqual(calc.sumar(-1, 1), 0)
        self.assertEqual(calc.sumar(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
