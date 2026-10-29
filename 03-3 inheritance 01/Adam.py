
class Adam:
    # 1. Parameterized constructor
    # Python does not support multiple constructors directly.
    # We can use default parameter values instead.
    def __init__(self, name="Unknown", eyeColor="Unknown",skinColor="Unknown"):
        self.name = name
        self.__eyeColor = eyeColor
        self._skinColor=skinColor

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
        

