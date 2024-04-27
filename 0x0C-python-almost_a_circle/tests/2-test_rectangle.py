import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_rectangle_creation(self):
        # Test cases for valid inputs
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 3)

        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

if __name__ == '__main__':
    unittest.main()
