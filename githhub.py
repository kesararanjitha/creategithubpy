class STUDENT:
    def __init__(self, name='Ran', roll=57):
        self.name = name
        self.roll = roll

    def display(self):
        print("Hello I am Sri")
        return f"My name is {self.name} and roll number is {self.roll}"


s = STUDENT()
print(s.display())
