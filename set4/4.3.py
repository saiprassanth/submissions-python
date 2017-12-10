'''program to convert usd to other currencies
saiprassanth
10dec2017'''
class money:
  def __init__(self,dollars,cents):
    '''function that assigns tha dollar and cent to self'''
    self.d=dollars
    self.c=cents
  def repre(self):
    '''method that returnds the money in the specified fomat'''
    print "$",self.d,".",self.c
  def add(self,dollars,cents):
    '''method to add some amount'''
    d=self.d+dollars
    c=self.c+cents
    print "$",d,".",c
  def dollar_to_inr(self):
    '''converts dollar to idian rupee'''
    d=self.d*64.48
    c=self.c*0.6448
    print "inr",d+c
  def dollar_to_dhiram(self):
    '''converts dollar to UAE dhiram'''
    d=self.d*3.67
    c=self.c*0.0367
    print "aed",d+c
  def dollar_to_ringget(self):
    '''converts dollar to malaysian ringgit'''
    d=self.d*4.08
    c=self.c*0.0408
    print "myr",d+c
d=int(raw_input("enter the dollars"))
c=int(raw_input("enter the cents"))
obj=money(d,c)
'''object creation and __init__ call'''
obj.repre()
obj.add(10,0)
obj.dollar_to_inr()
obj.dollar_to_dhiram()
obj.dollar_to_ringget()