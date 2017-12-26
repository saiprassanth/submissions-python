'''GCD
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is a test function",GCD(20,30)
  print "this is a test function",GCD(20,0)
  print "this is a test function",GCD(0,30)
def GCD(a,b):
  try:
    if b==0:
  
      return a
  
    else:
  
      r=a%b#storing the remainder
  
      return GCD(b,r)#recursive function call with second value and the remainder
  except:
    print "error"

a=int(raw_input('enter the first number'))

b=int(raw_input('enter the second number'))

print GCD(a,b)
test()