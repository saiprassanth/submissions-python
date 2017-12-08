'''program to find lcm betweem two numbers
saiprassanth.ramesh@accenture.com
8dec2017'''
def gcd(a,b):
  '''function to fing the gcd of two numbers'''
  try:  
    if b==0:
      return a
    else:
      return gcd(b,a%b)
  except ZeroDivisionError as e:
    print e
def lcm(a,b):
  '''function to find the lcm using gcd'''
  if a==0:
    return 0
  if b==0:
    return 0
  c=gcd(a,b)
  lcm=a*b/c#formula for finding lcm using gcd
  return lcm
def test():
  print 'this is a test function'
  print '2,3 \t',lcm(2,3),'\tecpected result is 6'
  print '6,3 \t',lcm(6,3),'\tecpected result is 6'
  print '0,3 \t',lcm(0,3),'\tecpected result is 0' 
print lcm(2,3)
test()