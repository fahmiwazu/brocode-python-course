class Car:

    wheels = 4  #class variable

    def __init__(self,make,model,year,color):
        self.make = make        #instant variable
        self.model = model      #instant variable
        self.year = year        #instant variable
        self.color = color      #instant variable

    def drive(self):
        print("this "+self.model+" is driving")

    def stop(self):
        print("this "+self.model+" is stop")