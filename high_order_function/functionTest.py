import unittest
# import function which will be testing

from unit_test import myAdd

from unit_test import mySub


class Test(unittest.TestCase):

    def setUp(self):
        print("before test")

    def tearDown(self):
        print("after test")

    def test_myAdd(self):
        self.assertEqual(myAdd(1, 2), 3, "add is wrong")
    def test_mySub(self):
        self.assertEqual(mySub(4,2),2,"sub is wrong")


if __name__ == '__main__':
    unittest.main()
