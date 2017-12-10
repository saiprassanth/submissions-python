'''program to find the area of a square using class
saiprassanth
10dec2017'''
class shape:
  '''parent class shape'''
  def area(self):
    '''method that returns area =0 by default'''
    return 0
class square(shape):
  '''subclass square '''
  def __init__(self,l):
    '''init function that assigns the length to self.length'''
    self.length=l
  def area(self):
    '''method that returns the area of the square of the given lenth'''
    return self.length*self.length
length=int(raw_input("enter the length of the square"))
obj=square(length)
'''object creation for base class'''
print obj.area()
'''calling the area method in the subclass'''