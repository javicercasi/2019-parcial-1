import unittest
from parcial import codigo


class Test(unittest.TestCase):

    def test_decimal_3(self):
        resultado = codigo(3)
        self.assertEqual(resultado, '3')

    def test_decimal_5(self):
        resultado = codigo(5)
        self.assertEqual(resultado, '5')
    
    def test_decimal_6(self):
        resultado = codigo(6)
        self.assertEqual(resultado, '6')

    def test_decimal_7(self):
        resultado = codigo(7)
        self.assertEqual(resultado, '7')

    def test_decimal_8(self):
        resultado = codigo(8)
        self.assertEqual(resultado, '8')

    def test_decimal_9(self):
        resultado = codigo(9)
        self.assertEqual(resultado, '9')


    def test_decimal_10(self):
       resultado=codigo(10)
       self.assertEqual(resultado, 'A')

    def test_interfaz_decimal_17(self):
       resultado=codigo(17)
       self.assertEqual(resultado, '11')

    def test_interfaz_decimal_16(self):    
       resultado=codigo(16)
       self.assertEqual(resultado, '10')

    def test_interfaz_decimal_4095(self):    
       resultado=codigo(4095)
       self.assertEqual(resultado, 'FFF')




if __name__ == '__main__':
   unittest.main()