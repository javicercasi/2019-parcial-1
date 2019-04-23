import unittest
from interfaz import interfaz


class TestInterfazDecimal(unittest.TestCase):
    def test_interfaz_decimal_5(self):
       result=interfaz(5)
       self.assertEqual(result, '5')

   

    def test_interfaz_decimal_17(self):     
       result=interfaz(17)
       self.assertEqual(result, '11')


    def test_interfaz_hola(self):
        result=interfaz('hola')
        self.assertEqual(result,'Error')

    def test_interfaz_factorial_vacio(self):
        result=interfaz('')
        self.assertEqual(result,'Error')


if __name__ == '__main__':
   unittest.main()