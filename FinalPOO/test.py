import unittest
class TestDni(unittest.TestCase):
    dni: str
    def setUp(self):
        self._dni = "43.123.456"
    def test_longitud(self):
        self.assertEqual(len(self._dni), 8)
    def test_punto(self):
        self.assertTrue("." not in self._dni)

if __name__ == '__main__':
    unittest.main()
