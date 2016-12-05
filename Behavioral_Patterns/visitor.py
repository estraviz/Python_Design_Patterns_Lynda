class House(object):
    """ The class being visited """

    def accept(self, visitor):
        """ Interface to accept a visitor """

        # Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        # We have a reference to the HVAC (Heating, ventilation and air conditioning) specialist object in the House object
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        # We now have a reference to the electrician object in the House object
        print(self, "worked on by", electrician)

    def __str__(self):
        """ Return the class name when the House object is printed """

        return self.__class__.__name__


class Visitor(object):
    """ Abstract visitor """

    def __str__(self):
        """ Return the class name when the Visitor object is printed """

        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """ Concrete visitor: HVAC specialist. Inherits from the parent class, Visitor """

    def visit(self, house):
        # The visitor now has a reference to the House object
        house.work_on_hvac(self)


class Electrician(Visitor):
    """ Concrete visitor: electrician. Inherits from the parent class, Visitor """

    def visit(self, house):
        # The visitor now has a reference to the House object
        house.work_on_electricity(self)


# Create an HVAC specialist
one_hvac_specialist = HvacSpecialist()

# Create an electrician
one_electrician = Electrician()

# Creat a house
one_house = House()

# Let the house accept the HVAC specialist and work on the house by invoking the visit() method
one_house.accept(one_hvac_specialist)

# Let the house accept the electrician and work on the house by invoking the visit() method
one_house.accept(one_electrician)
