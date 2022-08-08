def sum_of_natural_numbers(n):
    s=0
    for i in range(1,n+1):
        s=s+i

    print("Sum Of Natural Numbers: "+str(s))
def factorial_numbers(n):
    fact=1
    for i in range(1, n + 1):
        fact = fact * i

    print("The factorial of the number is : "+str(fact))

def print_factors(n):
   for i in range(1, n + 1):
       if((n%i)==0):
           print(i)

loop=True;
while(loop):
    print("1.To Find Sum Of Natural Numbers\n2.To Find Factorial Of A Number\n3.To Find Factors Of A Number\n4.EXIT\nEnter Your Choice: ")
    ch=int(input())
    if(ch==1):
        sum_of_natural_numbers(int(input("Enter a Number To Find: ")))
    elif(ch==2):
        factorial_numbers(int(input("Enter a Number To Find: ")))
    elif(ch==3):
        print_factors(int(input("Enter a Number To Find: ")))
    elif(ch==4):
        loop=False
    else:
        print("Enter a Correct Number To Find")