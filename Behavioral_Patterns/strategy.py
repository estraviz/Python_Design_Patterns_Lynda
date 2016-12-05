import types

class Strategy:
    """ The Strategy Pattern class """

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            # This allows us to binding dynamically the new method to the class
            self.execute = types.MethodType(function, self)

    def execute(self):
        # This gets replaced dynamically by another version if another strategy is provided
        """ The default method that prints the name of the strategy being used """

        print("{} is used\n".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1\n".format(self.name))

# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2\n".format(self.name))

# Let's create our default strategy
default_strategy = Strategy()

# Let's execute our default strategy
default_strategy.execute()

# Let's create the first variation of our default strategy by providing a new behavior
first_new_strategy = Strategy(function=strategy_one)

# Let's set its name
first_new_strategy.name = "First variation of the default strategy"

# Let's execute the strategy
first_new_strategy.execute()

# Now the same with a second variation of the default strategy and a new behavior
second_new_strategy = Strategy(function=strategy_two)
second_new_strategy.name = "Second variation of the default strategy"
second_new_strategy.execute()
