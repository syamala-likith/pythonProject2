import random

n = random.randbytes(3)
print(n)
print(random.randrange(1, 8))
print(random.randint(100, 211))
mylist = ["name", "age", "branch"]
mylist1 = ["likith", "sai", "reddy"]
dict = {'name': "likith", 'age': 19, 'branch': "CSE"}
print(random.choice(mylist1))  # will print any name in the list
print(random.getrandbits(1))  # will print boolean
print(random.choice(range(1, 101)))