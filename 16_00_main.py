# -*- coding: utf-8 -*-
"""Day-16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zMtw0LOmAk2-M5SbV0PwUEAfRKLO06VU
"""

print("Welcome To Day-16")

"""### Welcome to Day 16

## Classes & Objects in Python
"""

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

class StringReverse:
    def __init__(self, string):
        self.string = string
    
    def reverse(self):
        old_string = self.string
        new_string = ""

        for ch in old_string:
            new_string = ch + new_string

        return new_string

        # abc => cba
        # a + "" = a
        # b  + a = ba
        # c + b a = cba

        #  def   => f + ed => fed

sr = StringReverse("abcdef")
reversed_string = sr.reverse()
print(reversed_string)