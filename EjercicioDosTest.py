import unittest
import EjercicioDos

class TestEjercicioDos(unittest.TestCase):

    def testEsPar(self):
        par = EjercicioDos.esPar(6)
        self.assertEquals(par,True)
if __name__ == "__main__":
    unittest.main()