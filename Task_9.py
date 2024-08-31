class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

print(Car("Toyota", "Corolla", 2020).display_info())
