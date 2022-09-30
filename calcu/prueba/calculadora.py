class Calculator:
    def __init__(self):
        self.value = 0

    def suma(self, a, b):
        self.value = a + b

    def resta(self, a, b):
        self.value = a - b

    def multiplicacion(self, a, b):
        self.value = a * b

    def division(self, a, b):
        self.value = a / b

    def factorial(numero):
        fact = 1
        for i in range(1,numero+1):
            fact = fact * i
        return fact