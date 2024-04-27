import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_assign_id_automatically(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_assign_custom_id(self):
        base = Base(89)
        self.assertEqual(base.id, 89)

    # Add more test methods for other functionalities

if __name__ == '__main__':
    unittest.main()
