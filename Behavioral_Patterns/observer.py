class Subject(object):
    """ Represents what is being observed """

    def __init__(self):
        self._observers = []
        # This is where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject
        # to be observed by multiple _observers

    def attach(self, observer):
        # If the observer is not already in the observers list, append it to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # Remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # Alert all the observers in the list
        # Don't notify the observer who is actually updating the temperature
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    """ Inherits from the Subject class """

    def __init__(self, name=""):
        Subject.__init__(self)

        # Set the name of the core
        self._name = name

        # Initialize the temperature of the core.
        self._temp = 0

    @property
    # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter
    # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers when somebody changes the core temperature
        self.notify()

class TempViewer:
    """ This is an observer class """

    def update(self, subject):
        # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# Let's create our objects
core1 = Core("Core 1")
core2 = Core("Core 2")

# Let's create our observers
observer1 = TempViewer()
observer2 = TempViewer()

# Let's attatch our observers to the first core
core1.attach(observer1)
core1.attach(observer2)

# Let's change the temperature of our first core so the observers get notified
core1.temp = 80
core1.temp = 90
