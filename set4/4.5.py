'''program to find if two sets of coordinates are the same and return the coorndinates in such a format that object with same values can be created
saiprassanth
10dec2017'''
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getX(self):
    # Getter method for a Coordinate object's x coordinate.
    # Getter methods are better practice than just accessing an attribute directly
    return self.x

  def getY(self):
    # Getter method for a Coordinate object's y coordinate
    return self.y

  def __str__(self):
    return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

  def eq(self, other):
    '''returns True if coordinates refer to same point in the plane'''
    if self.x==other.x and self.y==other.y:
      return True
    else:
      return False
        
  def repr(self):
    '''returns a string that looks like a valid Python expression that could be used to recreate an object with the same value'''
    print 'Coordinate(',self.getX(),',',self.getY(),')'

x=int(raw_input("enter the first x coordinate"))
y=int(raw_input("enter the first y coordinate"))
x1=int(raw_input("enter the second x coordinate"))
y1=int(raw_input("enter the second y coordinate"))
c1 = Coordinate(x,y)
c2 = Coordinate(x1,y1)
print "are the coordinates same\n it is ",c1.eq(c2)
c1.repr()
