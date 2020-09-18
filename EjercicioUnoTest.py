import unittest
import EjercicoUno

class TestEjercicoUno(unittest.TestCase):

    def testConocerEdad(self):
        edad = EjercicoUno.conocerEdad(15,2020)
        self.assertEquals(edad, 65)
if __name__ == "__main__":
    unittest.main()