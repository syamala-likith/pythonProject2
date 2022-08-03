from Train import Train



class Booking(Train):

    def __init__(self,tname,tno,name,age,no_of_seats,gender):
        super().__init__(tname,tno)
        self.name=name
        self.age=age
        self.no_of_seats=no_of_seats
        self.gender=gender

    def display_details(self):
        self.display()
        print("Name: {}\nGender: {}\nAge: {}\nNo Of Seats: {}\nYour Booking Was Successfull".format(self.name,self.gender,self.age,self.no_of_seats))


obj=Booking(input("Enter Train Name: "),int(input("Enter Train Number: ")),input("Enetr Your Name: "),input("Enter Your Age: "),int(input("Enter Number Of Seats To Be Booked: ")),input("Enter Gender: "))
obj.display_details()