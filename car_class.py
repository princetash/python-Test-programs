class Car:
    def __init__(self, make, model, year):
        """initializing car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0
    

    def get_descriptive_name(self):
        """return neatly formatted name"""
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    

    def read_odemeter(self):
        print(f"This cars has {self.odemeter_reading} miles on it.")


    def update_odemeter(self,mileage):
        """setting odemeter to a certain value and rejecting attempts to roll it back"""
        if mileage >= self.odemeter_reading:
            self.odemeter_reading = mileage
        else:
            print("You cannot roll back the odemeter")

    
    def increament_odemeter(self, miles):
        """adding a specific value for the reading"""
        if miles > 0:
            self.odemeter_reading += miles
        else:
            print("You cannot roll back the odemeter")

my_car = Car("audi", 'a4', 2018)
print(my_car.get_descriptive_name())
# my_car.odemeter_reading = 2
my_car.update_odemeter(4)
my_car.increament_odemeter(20)
#my_car.update_odemeter(4)
# my_car.increament_odemeter(-10)
my_car.read_odemeter()