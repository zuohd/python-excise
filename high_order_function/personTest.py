import unittest
from person import Person

# p=Person("soderberg",20)
# print(p.getVar("name"))

class personTest(unittest.TestCase):
    def test_init(self): #need to add test prefix
        p=Person("Jack",34)
        self.assertTrue(p.name=="Jack","name assginment is wrong")
    def test_getAge(self):
        p=Person("Jack",34)
        self.assertEqual(p.getAge(),p.age,"getvar method is wrong")


if __name__ == '__main__':
    unittest.main()