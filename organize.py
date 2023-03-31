class Student:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel

    def studenthi(self):
        print(f'my name is {self.name}')
stu=Student('ni',12,122)
T=stu.studenthi()
