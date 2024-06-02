class student:
  def __init__(self,name,rollno):
    self.name=name
    self.rollno=rollno
  def display(self):
    print(f"My name is self.name and rollno is self.rollno")
name=input("Enter your name: ")
rollno=int(input("Enter your rollno: ")
s=student(name,rollno)
s.display()
