class Car:
    def __init__(self):
        self.__color =""
        self.__model =""
        self.__year =0

    def set_color(self,color):
        self.__color=color

    def get_color(self):
        return self.__color

    def set_model(self,model):
        self.__model=model

    def get_model(self):
        return self.__model
    
    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year



    # Display attributes from inside the class
    def display_info(self):
        print("Color:", self.__color)
        print("Model:", self.__model)
        print("Year:", self.__year)

    def __start(self):
        print("Car started")

    def __move(self):
        print("Car is moving")

    def __stop(self):
        print("Car stopped")
    
    def run(self):
        self.__start()
        self.__move()
        self.__stop()


# Create an object
obj1 = Car()
obj1.set_color("red")
obj1.set_model("Toyota")
obj1.set_year(2026)
obj1.display_info()
# obj1.__start()
obj1.run()
