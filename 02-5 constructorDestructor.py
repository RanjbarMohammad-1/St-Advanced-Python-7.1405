
class Car:

    # Constructor
    def __init__(self, color, model, year):
        print("Constructor: Car object created")

        # Public attribute
        self.color = color

        # Protected attribute (naming convention)
        self._model = model

        # Private-style attribute (name mangling)
        self.__year = year

    # Getter and setter for the private-style attribute
    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    # Display car information
    def display_info(self):
        print("Color:", self.color)
        print("Model:", self._model)
        print("Year:", self.__year)

    # Private-style methods
    def __start(self):
        print("Car started")

    def __move(self):
        print("Car is moving")

    def __air_conditioner(self):
        print("Air conditioner is on")

    def __stop(self):
        print("Car stopped")

    # Public method that calls the private-style methods
    def run(self):
        self.__start()
        self.__air_conditioner()
        self.__move()
        self.__stop()

    # Destructor
    def __del__(self):
        print("Destructor: Car object is being destroyed")


# Create an object
car1 = Car("Red", "Toyota", 2025)

print("\n=== PUBLIC ATTRIBUTE ===")
print(car1.color)
car1.color = "Blue"
print(car1.color)

print("\n=== PROTECTED ATTRIBUTE ===")
print(car1._model)
car1._model = "BMW"
print(car1._model)

print("\n=== PRIVATE-STYLE ATTRIBUTE ===")
print(car1.get_year())
car1.set_year(2030)
print(car1.get_year())

# Direct access to the original name raises AttributeError
try:
    print(car1.__year)
except AttributeError:
    print("Cannot access __year using its original name")

print("\n=== CAR INFORMATION ===")
car1.display_info()

print("\n=== PRIVATE-STYLE METHODS ===")
car1.run()

print("\n=== NAME MANGLING ===")
print("Year using mangled name:", car1._Car__year)

print("\n=== DESTROY OBJECT ===")
del car1

print("End of program")
