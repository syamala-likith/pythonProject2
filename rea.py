import re
# txt = "Use of python in machine Learning"
# x = re.search("^Use.*Learning$", txt)
# if (x):
#     print("Yes!")
# else:
#     print("no")
# print(x)
# y=re.findall("in",txt)
# print(y)
txt = "Python is one of the most popular languages"
x = re.search("\s", txt)
if (x):
    print("White Space is located")
else:
    print("no")
