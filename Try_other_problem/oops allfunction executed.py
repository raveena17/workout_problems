class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.height + 2 * self.width

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getStats(self):
        return "area:      %s\nperimeter: %s" % (self.area(), self.perimeter())


def main():
    print ""
    print "Rectangle a:"
    a = Rectangle(5, 7)
    print "area:      %s" % a.area()
    print "perimeter: %s" % a.perimeter()

    print ""
    print "Rectangle b:"
    b = Rectangle()
    b.width = 10
    b.height = 20
    print b.getStats()
    print ""
