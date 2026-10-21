class Car:
    color = "Red"
    _model = "Toyota"
    __year = 2025

car1 = Car()



car1.__year=100
print(car1.color)
print(car1._model)
print(car1.__year)