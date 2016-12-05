class DrawingAPIone(object):
    """ Implementation-specific abstraction: concrete class one """

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {})".format(x, y, radius))


class DrawingAPItwo(object):
    """ Implementation-specific abstraction: concrete class two """

    def draw_circle(self, x, y, radius):
        # Same interface as in DrawingAPIone but different implementation
        print("API 2 drawing a circle at ({}, {} with radius {})".format(x, y, radius))


class Circle(object):
    """ Implementation-independent abstraction: for ex., there could be a rectangle class """

    def __init__(self, x, y, radius, drawing_api):
        """ Initialize the necessary attributes """

        self._x = x
        self._y = y
        self._radius = radius
        # the next argument accepts an instance of our DrawingAPIone or DrawingAPItwo classes
        self._drawing_api = drawing_api

    def draw(self):
        """ Implementation-specific abstraction taken care of by another class: DrawingAPI """

        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """ Implementation-independent """

        self._radius *= percent


# Build the first Circle object using API one
circle1 = Circle(1, 2, 3, DrawingAPIone())
# Draw a Circle
circle1.draw()

# Build the Second object using API two
circle2 = Circle(2, 3, 4, DrawingAPItwo())
# Draw a Circle
circle2.draw()
