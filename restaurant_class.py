class Restaurant:
    def __init__(self, resta_name, cuisine_type):
        self.name = resta_name
        self.cuisine = cuisine_type
        self.served = 0
    

    def decsribe_restaurant(self):
        print(f"{self.name} is an italian restaurant")
        print(f"To get all the best {self.cuisine} cuisines, go to {self.name} restaurant")


    def open_restaurant(self):
        print(f"{self.name} is now open, with {self.cuisine + 's'} available")


    def set_number_served(self, served_customers):
        self.served = served_customers
        print(f"We have served {self.served} customers")


    def increament_number_served(self, increased_customers):
        self.served += increased_customers
        print(f"We have served {self.served} customers")


restaurant1 = Restaurant("Teatot", "Burger")
restaurant1.decsribe_restaurant()
restaurant1.open_restaurant()


#restaurant1.served = 6
restaurant1.set_number_served(5)
restaurant1.increament_number_served(100)



class icecream_stand(Restaurant):
    def __init__(self, resta_name, cuisine_type):
        super().__init__(resta_name, cuisine_type)
        self.flavour = "best", "good"

    
    def flavours(self):
        print(f"These are the available flavours {self.flavour}")


icecreamStand = icecream_stand("Tips", "Cheese")
icecreamStand.flavours()