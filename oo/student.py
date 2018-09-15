from  person import Person

class Student(Person):
    def __init__(self,name,age,stuId):
        #calling super class construction
        super(Student,self).__init__(name,age)
        self.stuId=stuId
    def study(self):
        pass