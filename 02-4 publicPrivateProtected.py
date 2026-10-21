class Car:
    def __init__(self):
        # 1. PUBLIC attribute
        self.color = "Red"

        # 2. PROTECTED attribute (convention)
        self._model = "Toyota"

        # 3. PRIVATE-style attribute (name mangling)
        self.__year = 2025

    # Methods to access the attributes
    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    # Display attributes from inside the class
    def display_info(self):
        print("Color:", self.color)
        print("Model:", self._model)
        print("Year:", self.__year)

    def start(self):
        print("Car started")

    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


# Create an object
car1 = Car()
print("========== 1. PUBLIC ==========")
# Direct access is allowed
print(car1.color)
car1.color = "Blue"
print(car1.color)
print("\n========== 2. PROTECTED ==========")
# Direct access is possible in Python,
# but discouraged by convention
print(car1._model)
car1._model = "BMW"
print(car1._model)
print("\n========== 3. PRIVATE-STYLE ==========")
# Access through getter
print(car1.get_year())
# Change through setter
car1.set_year(2026)
print(car1.get_year())
# print("car1.__year =")
# print(car1.__year)
# Direct access using the original name fails
try:
    print(car1.__year)
except AttributeError:
    print("Cannot access car1.__year directly!")
car1.__year=32
print(car1.__year)

print("\n========== INSIDE THE CLASS ==========")

# The class can access all three attributes
car1.display_info()


print("\n========== CAR OPERATIONS ==========")

car1.start()
car1.move()
car1.stop()
