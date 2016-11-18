class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y

point = Point()
point.print_point()

point = Point(15)
point.print_point()

point = Point(40, 50)
point.print_point()
