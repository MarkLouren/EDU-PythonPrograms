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
