import unittest


class SimpleTest(unittest.TestCase):
    def test_pass(self):
        assert 1 == 1, 'Some how 1 is not equal to 1'

        # NOTE: *NEVER* do this
        assert(1 == 2, 'this is the same as `assert tuple(Flase, "...")` which is *always* True')

        self.assertTrue(1 == 1, 'Some how 1 is not equal to 1')
        self.assertEqual(1, 1, 'Some how 1 is not equal to 1')

    def test_fail(self):
        self.assertFalse(True, 'what? True is not False?')

    def test_raises(self):
        def raise_test():
            raise ValueError('this is bad')

        self.assertRaises(ValueError, raise_test)

# this is so if we run the script manually
#   python 1_unittest/1_simple.py
# then the test cases will be run for us
if __name__ == '__main__':
    unittest.main()
