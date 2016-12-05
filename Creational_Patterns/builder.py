class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """ Abstract Builder """

    def __init__(self):
        # calls the Car object below and keeps it as its attribute
        self.car = None

    def create_new_car(self):
        self.car = Car()


class FerrariBuilder(Builder):
    # Inherits from the abstract builder class but provides methods to be used by the Director class eventually
    """ Concrete Builder --> provides parts and tools to work on the parts """

    def add_model(self):
        self.car.model = "Ferrari F40"

    def add_tires(self):
        self.car.tires = "Pirelli P-Zero tires"

    def add_engine(self):
        self.car.engine = "V8 engine"


class RenaultBuilder(Builder):
    # Inherits from the abstract builder class but provides methods to be used by the Director class eventually
    """ Concrete Builder --> provides parts and tools to work on the parts """

    def add_model(self):
        self.car.model = "Renault Megane"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Petrol engine"


class Car():
    """ Product """

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}\n'.format(self.model, self.tires, self.engine)


builder = FerrariBuilder()
director = Director(builder=builder)

# Construct the car by invoking the construct_car method
director.construct_car()
car = director.get_car()

print(car)

# we repeat the process for another car after including another concrete builder class
renaultBuilder = RenaultBuilder()
renaultDirector = Director(builder=renaultBuilder)
renaultDirector.construct_car()
anotherCar = renaultDirector.get_car()
print(anotherCar)
