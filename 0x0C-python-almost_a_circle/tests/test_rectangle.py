import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor_with_no_arguments(self):
        r = Rectangle()
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_constructor_with_arguments(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 6)

    def test_width_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 3)

    def test_height_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2, -3)


if __name__ == '__main__':
    unittest.main()
