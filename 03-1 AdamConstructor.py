
class Adam:

    # 1. Parameterized constructor
    # Python does not support multiple constructors directly.
    # We can use default parameter values instead.
    def __init__(self, name="Unknown", eyeColor="Unknown"):
        self.name = name
        self.__eyeColor = eyeColor

        print("Constructor called.")

    # 2. Destructor
    def __del__(self):
        print("Destructor called for", self.name)

    # 3. Getter for the private attribute
    def get_eyeColor(self):
        return self.__eyeColor

    # 4. Setter for the private attribute
    def set_eyeColor(self, eyeColor):
        self.__eyeColor = eyeColor

    # 6. Public method
    def walk(self):
        print(self.name, "is walking.")

    # 7. Private method
    def __speakWithGOD(self):
        print("Adam can speak with GOD")

    # 8. protected method
    def _pray(self):
        print(self.name, "is praying.")

    # 9. Public method to display all properties
    def introduce(self):
        print("Name:", self.name)
        print("Eye Color:", self.__eyeColor)



print(3*"\n")
print("=============Create an object  using the default values================")
# Create an object using the default values
adam1 = Adam()
adam1.introduce()
print("=============Create an object using parameters================")
# Create an object using parameters
adam2 = Adam("Adam", "Brown")
print("Adam(Adam, Brown)")
adam2.introduce()
print("============= other method ================")
# Access the public attribute
print("Name:", adam2.name)
# Access the private attribute through the getter
print("Eye color:", adam2.get_eyeColor())
# Change the private attribute through the setter
adam2.set_eyeColor("Blue")
print("New eye color:", adam2.get_eyeColor())
# Call the public method
adam2.walk()

