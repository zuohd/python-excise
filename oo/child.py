from father import Father
from monther import Mother

'''
multiple super classes inherit
'''
class Child(Father, Mother):
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)
