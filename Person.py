# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname;
#         self.lname=lname;
#     def printname(self):
#         print(self.fname,self.lname)
#
# x=Person("Likith","Sai")
# x.printname()
class Parent:
    def __init__(self, text):
        self.msg = text;

    def printmsg(self):
        print(self.msg)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


x = Child("Hello, and Welcome!")
x.printmsg()
