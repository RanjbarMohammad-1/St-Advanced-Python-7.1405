class Adam:

    def __init__(self,name,eyeColor):
        self.name=name
        self.__eyeColor=eyeColor
        print("this is constructor")
        print("we are create an object with name of  ",name)

    def __del__(self):
        print("Destructor called for", self.name)


    def get_eyeColor(self):
        return self.__eyeColor
    def set_eyeColor(self,eyeColor):
        self.__eyeColor = eyeColor

adam2=Adam("ali","Khormay")
print(adam2.name)

# adam1=Adam("nadia")
# print (adam1.name)
# adam2.set_eyeColor("red")
# print(adam2.get_eyeColor())
# print(adam2.get__eyeColor())
