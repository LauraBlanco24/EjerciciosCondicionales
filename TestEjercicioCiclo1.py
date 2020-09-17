import unittest
import EjercicioCiclo1

class TestEjercicioCiclo1(unittest.TestCase):

    def testpalindroma(self):
        EjercicioCiclo1.palindroma("oso")
if __name__ == "__main__":
    unittest.main()