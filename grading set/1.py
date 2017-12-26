'''2D array
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is test",fun(0,0)
  print "this is test",fun(3,0)
  print "this is test",fun(0,3)
def fun(x,y):
  try:
    matrix=[[0 for a in range(y)]for b in range(x)]#initializing the array for the specified size
    for a in range(x):
      for b in range(y):
        matrix[a][b]=a*b#changing the values of the array to product of row and column number 
    return matrix
  except:
    print "error"
x=int(raw_input("enter the no of rows"))
y=int(raw_input("enter the no of columns"))
print "this is main function",fun(x,y)
test()