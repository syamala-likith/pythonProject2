class Train:
    def __init__(self,tname,tno):
        self.tname=tname;
        self.tno=tno;
    def display(self):
        print("\nTrain Name: {}\nTrain Number: {}".format(self.tname,self.tno))