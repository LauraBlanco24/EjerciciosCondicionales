import unittest
import EjercicioTres

class TestEjercicioTres(unittest.TestCase):

    def testConocerEdad(self):
        palabra = EjercicioTres.palabras('Hola')
        self.assertEquals(palabra, ('H','a'))
if __name__ == "__main__":
    unittest.main()