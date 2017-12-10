'''program to return the gender based on the class
saiprassanth
10dec2017'''
class person:
  '''base class person'''
  def __init__(self):
    pass
class male(person):
  '''subclass male '''
  def __init__(self):
    '''init function that assigns male to value '''
    self.value='male'
  def getgender(self):
    '''returns the gender'''
    print 'inside male class'
    return self.value
class female(person):
  '''subclass female'''
  def __init__(self):
    '''init function that assigns female values to the variable'''
    self.value='female'
  def getgender(self):
    '''return the gender'''
    print 'inside female class'
    return self.value
o1=male()
print o1.getgender()
o2=female()
print o2.getgender()