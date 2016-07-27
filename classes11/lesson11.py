class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print self.time

clock = Clock('5:30')
clock.print_time()

class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print time

clock = Clock('5:30')
clock.print_time('10:30')


class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        assert type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

c1 = Coordinate(17,38)
c2 = Coordinate(17,38)
c3 = Coordinate(1,-8)

print c1
print repr(c1)
print c1 == c2
print c2 == c3


class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8
w1 = Weird(X, Y)
#print w1.getX()
w2 = Wild(X, Y)
print w2.getX()
w3 = Wild(17, 18)
print w3.getX()
w4 = Wild(X, 18)
print w4.getX()
X = w4.getX() + w3.getX() + w2.getX()
print X
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print Y
print w2.getY()