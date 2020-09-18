import unittest
import EjercicioCiclo2

class TestEjercicioCiclo2(unittest.TestCase):

    def test_multiplos(self):
        EjercicioCiclo2.multiplos(2,21,3)
if __name__ == "__main__":
    unittest.main()