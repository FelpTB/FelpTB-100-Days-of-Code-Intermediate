def add(*args):
    result = 0
    for n in args:
        result = result+n
    return result


def calculate(n, **kwargs):
    # for key ,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n -= kwargs["sub"]
    print(n)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.color = kw["color"]



#print(add(1,2,3,4,5,6,7,8,8,9))

carro = Car(color="red", make="fiat")
print(carro.color)
calculate(3,add=3, sub=2)



