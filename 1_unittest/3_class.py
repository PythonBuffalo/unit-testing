import unittest


class MyClass(object):
    def __init__(self, numbers):
        self.numbers = set(numbers)

    def add_number(self, number):
        self.numbers.add(number)

    def add_numbers(self, numbers):
        self.numbers |= set(numbers)


class TestMyClass(unittest.TestCase):
    def test___init__(self):
        mc = MyClass([3, 4, 5, 6, 6, 6, 6])
        self.assertIsInstance(mc.numbers, set)
        self.assertEqual(mc.numbers, set([3, 4, 5, 6]))

        self.assertRaises(TypeError, MyClass, 7)

    def test_add_number(self):
        mc = MyClass([3, 4, 5])
        mc.add_number(5)
        mc.add_number(6)
        mc.add_number(3)
        self.assertEqual(mc.numbers, set([3, 4, 5, 6]))

    def test_add_numbers(self):
        mc = MyClass([3, 4, 5])
        mc.add_numbers([3, 4, 5, 6])
        self.assertEqual(mc.numbers, set([3, 4, 5, 6]))

        self.assertRaises(TypeError, mc.add_numbers, 5)


if __name__ == '__main__':
    unittest.main()
