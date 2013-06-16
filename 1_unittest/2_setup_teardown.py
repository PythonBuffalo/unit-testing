import unittest


class SetupTeardownTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """This is run before any of the test methods are run

        @classmethod is required
        """
        self.data = {'not': 'what', 'we': 'want'}

    @classmethod
    def tearDownClass(self):
        """This is run after all the test methods have been run

        @classmethod is required
        """
        self.data = None

    def setUp(self):
        """This is run before each and every test
        """
        self.data = {'some': 'data'}

    def tearDown(self):
        """This is run after each and every test
        """
        self.data = None

    def test_data(self):
        """Test and make sure that setUp is run before this test
        method and we get the data we expect
        """
        self.assertIsNotNone(self.data, 'self.data is None')
        self.assertEqual(self.data, {'some': 'data'}, 'self.data is not what we expected')

    def test_again(self):
        """Same as the test above just to prove that setUp is run
        again before this test method
        """
        self.assertIsNotNone(self.data, 'self.data is None')
        self.assertEqual(self.data, {'some': 'data'}, 'self.data is not what we expected')

if __name__ == '__main__':
    unittest.main()
