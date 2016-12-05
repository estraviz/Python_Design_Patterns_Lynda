import copy

class Prototype:

    def __init__(self):
        # Create a dictionary object that contains the objects that will be cloned
        self._objects = {}

    def register_object(self, name, obj):
        """ Register an object """
        # name is a name :) and will be used as a key when storing the object in the dictionary object
        # obj is the object to be cloned
        self._objects[name] = obj

    def unregister_object(self, name):
        """ Unregister an object """
        # delete the objects from the dictionary object
        del self._objects[name]

    def clone(self, name, **attr):
        """ Clone a registered object and update its attributes """
        # first we copy the object
        obj = copy.deepcopy(self._objects.get(name))
        # update its attributes if needed
        # __dict__ represents all the attributes of the object
        obj.__dict__.update(attr)
        return obj


class Car:

    def __init__(self):
        self.name = "BMW X5"
        self.color = "Red"
        self.options = "Special Edition"

    def __str__(self):
        # returns the attributes of the object when we print it
        return '{} | {} | {}\n'.format(self.name, self.color, self.options)


# first we instantiate the Car class. This is the prototypical object to be replicated or cloned
my_car = Car()

# create an instance of the Prototype class
prototype = Prototype()

# register it
prototype.register_object('bmw', my_car)

# let's clone that object
your_car = prototype.clone('bmw')

# and we print that cloned object
print(your_car)
