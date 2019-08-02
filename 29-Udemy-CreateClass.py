#Basics Class Creation
class MaxSizeList(object):

    def __init__(self, max_length):
        self.max_length = max_length
        self.ls=[]

    def push(self, st):
        self.ls.append(st)
        if len(self.ls)>self.max_length:
            self.ls.pop(0)

    def get_list(self):
        return self.ls

a=MaxSizeList(3)
a.push("BLa")
a.push("BLa")
a.push("BLa")
print(a.get_list())

#Inheritance

class Date(object):   #Inherits from the 'object' class
    def get_date(self):
        return '2014-10-13'

class Time(Date):    #inherits from the 'date' class
    def get_time(self):
        return '08:13:07'
tm=Time()
print (tm.get_date())

# Use super 

import random

class Animal(object):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
       super(Dog, self).__init__(name)  #super designed relate class to the parent class, in this case __init__ function from the parent, uses in order to illiminate code duplication
       self.breed = random.choice (["Shih Tzu", "Beagle", "Mutt"])

    def fetch(self, thing):
        print ('{} goes after the {}'.format(self.name, thing))

d=Dog('dogname')
print (d.fetch('meat'))

#Multiple inheritance

class A(object):
    def dothis(self):
        print ('doing this in A')

class B(A):
    pass

class C(object):
    def dothis(self):
        print ('doing this in C')

class D(B,C): #multiple inheritance
    pass

print (D.mro()) #order of class inheritance B,A,C

#Multiple inheritance Diamond shape patern
class A(object):
    def dothis(self):
        print ('doing this in A')

class B(A): 
    pass

class C(A): #C and B inherit from A so in order BACA, earlier A is removed
    def dothis(self):
        print ('doing this in C')

class D(B,C): #multiple inheritance
    pass

print (D.mro()) #order of class inheritance B,C,A

#СlassMethod Example
class InstanceCounter(object):
    count =0

    def __init__(self, val):
        self.val=val
        InstanceCounter.count +=1

    def set_val(self, newval):
        set.val = newval

    def get_val(self):
        return self.val

    @classmethod  #work with class and it's own attributes
    def get_count(cls):
        return  cls.count

a=InstanceCounter(5)
b=InstanceCounter(24)

for obj in (a,b):
    print (obj.get_val())
print (obj.get_count())  #two instances
