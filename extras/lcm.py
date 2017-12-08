'''program to find lcm betweem two numbers
saiprassanth.ramesh@accenture.com
8dec2017'''
def lcm(m,n):
  '''function to find the lcm'''
  if m>n:
    """assigning the maximum value to x"""
    x=m
  else:
    x=n
  try:  
    while True:
      if x%m==0 and x%n==0:
        '''finding if the maximum value is divisible by both numbers'''
        res=x
        return x
      x+=1
  except ZeroDivisionError as e:
    print e
def test():
  print 'this is a test function'
  print '3,8 \t',lcm(3,8),'expected result is 24'
  print '14,3 \t',lcm(14,3),'expected result is 42'
  print '0,3 \t',lcm(0,3),'expected result is integer division or modulo by zero'
  print lcm(3,6)
test()