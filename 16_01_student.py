class Student:

    #class variables
    university = "RGTU"


    # dunder method:  start end __
    def __init__(self, name, age):
        # instance variables:
        self.name = name
        self.age = age

    # print(obj) =>  call
    def __str__(self):
        return "{0} {1}".format(self.name, self.age)


s = Student("Amit", 20)
t = Student("raju", 21)
print(s)
print(s.university) # RGTU

# python => static variables



print(t.university)

# bina object ke bhi access kar skta hu
print(Student.university)

print(Student.university)

print(isinstance(s, Student))

obj = 12 # int
print(isinstance(obj, int))



# s   ->   __str__()

