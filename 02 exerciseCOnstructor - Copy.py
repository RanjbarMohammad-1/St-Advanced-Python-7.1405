class Car:

    def __start(self):
       print("car is start")
    def __move(self):
        print("car is moving")
    def run(self):
        self.__start()
        self.__move()
    def __init__(self,newColor):
        self.__color=newColor
        # self.model="benz"
    def set_color(self,inputColor):
        self.__color=inputColor
    def get_color(self):
        return self.__color
objCar2=Car("gray")
print(objCar2.get_color())


# objCar1=Car()
# objCar1.run()


# objCar1.__move()
# objCar1.move()
# print("objCar1.model=",objCar1.model)
# objCar1.set_color("green")
# print(objCar1.get_color())
# print("objCar1.__color=",objCar1.__color)

