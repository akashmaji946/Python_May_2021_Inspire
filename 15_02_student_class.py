class Student:
    # constructor
    def __init__(self):
        # attributes
        self.name = "Akash"
        self.age = 30

obj = Student()
print(obj.name)
obj.name = "Akaash"
print(obj.age)
obj.age = obj.age + 1

print(obj.name)
print(obj.age)