class Student:
  def __init__(self,name="ranjitha",rollno=57,age=19,gender="Female"):
    self.name=name
    self.rollno=rollno
    self.age=age
    self.gender=gender
  def display(self):
    print(f"Hi My name is {self.name} rollno : {self.rollno} age is {self.age} and gender : {self.gender}")
s=Student()
s.display()
