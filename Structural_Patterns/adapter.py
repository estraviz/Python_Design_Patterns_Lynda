class Korean:
    """ Korean speaker """

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "annyeong sesang!"


class British:
    """ English speaker """

    def __init__(self):
        self.name = "British"

    # Method with a different name!
    def speak_english(self):
        return "hello world!"


class Adapter:
    """ This changes the generic method name to individualized method names """

    def __init__(self, object, **adapted_method):
        """ Change the name of the method """

        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name:
        # speak() and the concrete method name such as speak_korean() or speak_english()
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """ Return the rest of the attributes """

        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to the objects list: we use the Adapter() as we want to change the mapping
# between the generic method call speak() to the individualized method names
objects.append(Adapter(korean, speak=korean.speak_korean)) # dictionary with speak as the key
objects.append(Adapter(british, speak=british.speak_english)) # british.speak_english is the value here

# for loop to invoke the individualized speak methods
for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
