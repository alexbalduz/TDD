# Cargamos el módulo unittest
import unittest
# Importamos la clase calculadora
from prueba.calculadora import Calculator

# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Creamos una prueba para probar un valor inicial
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    # Creamos un nuevo test para comprobar una suma
    def test_suma_method(self):
        # Ejecutamos el método
        self.calc.suma(1, 3)
        # Comprobamos si el valor es el que esperamos self.assertEqual(4, self.calc.value)
        self.assertEqual(4, self.calc.value)

        # Creamos un nuevo test para comprobar una resta
    def test_resta_method(self):
        # Ejecutamos el método
        self.calc.resta(1, 3)
        # Comprobamos si el valor es el que esperamos self.assertEqual(4, self.calc.value)
        self.assertEqual(-2, self.calc.value)

        # Creamos un nuevo test para comprobar una multiplicacion
    def test_multiplicacion_method(self):
        # Ejecutamos el método
        self.calc.multiplicacion(1, 3)
        # Comprobamos si el valor es el que esperamos self.assertEqual(4, self.calc.value)
        self.assertEqual(3, self.calc.value)

        # Creamos un nuevo test para comprobar una division
    def test_division_method(self):
        # Ejecutamos el método
        self.calc.division(4, 2)
        # Comprobamos si el valor es el que esperamos self.assertEqual(4, self.calc.value)
        self.assertEqual(2, self.calc.value)

    def test_factorial_method(self):
        # Ejecutamos el método
        self.calc.factorial(3)
        # Comprobamos si el valor es el que esperamos self.assertEqual(4, self.calc.value)
        self.assertEqual(6, self.calc.value)