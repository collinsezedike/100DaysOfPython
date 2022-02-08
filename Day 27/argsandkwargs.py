def add(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add(3, 4, 5, 4, 1))


def calculate(n=0, **kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")    
        self.model = kw.get("model")    
        self.color = kw.get("color")  


car = Car(make="Nissan", color="black")
print(car.color)
print(car.model)