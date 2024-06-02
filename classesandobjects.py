
class STUD:
    def __init__(self, name='Ran', roll=57, age=19, gender='female'):
        self.name = name
        self.roll = roll
        self.age = age
        self.gender = gender

    def display(self):

        print(f"Hi, my name is {self.name}, roll number: {self.roll}, age: {self.age}, and gender: {self.gender}")
        print("Hii every one")


s = STUD()
s.display()
