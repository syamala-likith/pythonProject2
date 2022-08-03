import math
class perimeter:

    def rect(self,a,b):
        print("Area of rectangle "+str(a*b))
        print("Perimeter of Rectangle "+str(2*(a+b)))
    def circle(self,r):
        print("Area of circle "+str(math.pi*math.pow(r,2)))
        print("perimeter of circle "+str(2*math.pi*r))
    # def triangle(self,a,b,c):
    #     h=math.sqrt((a*a)+(b*b))
    #     print("Area of Triangle "+str(math.pi*math.pow(r,2)))
    #     print("Perimeter of Triangle "+str(2*math.pi*r))

obj=perimeter()

print("Enter Number of inputs less than or equal to 2:")
ch=int(input())
if(ch==2):
    obj.rect(int(input("Enter 1st Side:")), int(input("Enter 2nd Side:")))
elif(ch==1):
     obj.circle(int(input("Enter Radius:")))
# elif(ch==3):
#     obj.triangle(int(input("Enter 1st Side:")), int(input("Enter 2nd Side:")),int(input("Enter 3rd Side:")))