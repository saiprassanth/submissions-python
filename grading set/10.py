'''fibonacci series using list comprehension
saiprassanth.ramesh@accenture.com
'''
def test():
  #this is a test function
  print "test function",",".join(str(i) for i in fun(6))
  print "test function",",".join(str(i) for i in fun(-10))
def fun(n):
  list= [0,1]
  if n==0:
    return list[0]
  elif n==1:
    return list
  elif n>1:
    [list.append(list[-2] +list[-1]) for x in range(n-1)]#using list comprehension to find the fibonacci series
    return list
  else: 
    print "enter a positive number"
try:
  n=int(raw_input("enter the index upto which  the fibonacci series is to be displayed"))
  print ",".join(str(i) for i in fun(n))#converting the integer list to a string
  test()
except TypeError as e:
  print e
