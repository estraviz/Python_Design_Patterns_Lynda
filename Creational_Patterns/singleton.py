class Borg:
    """ Borg class making class attributes global """
    # Attribute dictionary
    _shared_state = {}

    def __init__(self):
        # Make it an attribute dictionary
        self.__init__ = self._shared_state


class Singleton(Borg):
    # Inherits from the Borg class
    """ This class now shares all its attributes among its various instances """
    # This essentially makes the singleton object an object-oriented global variable
    # a global dictionary of acronyms

    def __init__(self, **kwgargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwgargs)

    def __str__(self):
        # Returns the attribute dictionary for printing when the print function is used
        return str(self._shared_state)


# Let's create a singleton object and add our first acronym
one_singleton_object = Singleton(HTTP = "Hyper Text Transfer Protocol")

# Print the object
print(one_singleton_object)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
another_singleton_object = Singleton(SNMP = "Simple Network Management Protocol")

# Print the object
print(another_singleton_object)
