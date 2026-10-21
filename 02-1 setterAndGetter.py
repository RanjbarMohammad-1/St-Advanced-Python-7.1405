class Car:
    # Private attributes
    __color = ""
    __model = ""
    __year = 0

    # Setter for color
    def set_color(self, color):
        self.__color = color

    # Getter for color
    def get_color(self):
        return self.__color

    # Setter for model
    def set_model(self, model):
        self.__model = model

    # Getter for model
    def get_model(self):
        return self.__model

    # Setter for year
    def set_year(self, year):
        self.__year = year

    # Getter for year
    def get_year(self):
        return self.__year

    def start(self):
        print("Car started")

    def move(self):
        print("Car is moving")

    def air_conditioner(self):
        print("Air conditioner is on")

    def stop(self):
        print("Car stopped")


# Create an object
car1 = Car()

# Set attributes using setters
car1.set_color("Red")
car1.set_model("Toyota")
car1.set_year(2025)


print("====================")
# Get attributes using getters
print("we get the attributes by getter")
print(car1.get_color())
print(car1.get_model())
print(car1.get_year())

print("====================")
print("call method")
# Call methods
car1.start()
car1.air_conditioner()
car1.move()
car1.stop()

print("====================")
car1.__hojfjodisjj=56
print(car1.__hojfjodisjj)
print(car1.__color)





