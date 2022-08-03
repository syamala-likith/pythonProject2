# def prime(n):
#     count = 0
#     for i in range(2, (n // 2) + 1):
#         if (n % i == 0):
#             count = count + 1
#     if (count == 0):
#         print("Number is Prime")
#     else:
#         print("Number is not Prime")
#
#
# prime(int(input("Enter any number: ")))

def prime(n):
    count = 0
    for i in range(2, (n // 2) + 1):
        if (n % i == 0):
            count = count + 1
    if (count == 0):
        print(n)


for i in range(1,101):
    prime(i)
