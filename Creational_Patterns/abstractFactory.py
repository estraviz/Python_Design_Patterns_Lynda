class Dog:
    """ One of the objects to be returned """

    def speak(self):
        return "Guau!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """ Concrete Factory """

    def get_pet(self):
        """ Returns a Dog object """
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"

class Cat:
    """ One of the objects to be returned """

    def speak(self):
        return "Miau!"

    def __str__(self):
        return "Cat"


class CatFactory:
    """ Concrete Factory """

    def get_pet(self):
        """ Returns a Cat object """
        return Cat()

    def get_food(self):
        """Returns a Cat Food object"""
        return "Cat Food!"


class PetStore:
    """ PetStore houses our Abstract Factory """

    def __init__(self, pet_factory=None):
        """ the attribute _pet_factory is our Abstract Factory """
        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display details of the objects returned by DogFactory """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!\n".format(pet_food))


# Instantiate a Concrete Factory that will be used by the Abstract Factory eventually
factory = DogFactory()

# Create a pet store which is housing our Abstract Factory in its attribute
shop = PetStore(pet_factory=factory)

# Invoke the utility method of the shop object to show the details of our pet
shop.show_pet()

# Now we could do the same with another concrete factory
factory = CatFactory()
shop = PetStore(factory)
shop.show_pet()
