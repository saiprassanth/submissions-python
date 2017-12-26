'''cube upto the specified limit in a dictionary
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is a test function",fun(0)
  print "this is a test function",fun(-5)
  print "this is a test function",fun(10)
def fun(limit):
  no=1
  sq=0
  dict={}#initializing an empty dictionary
  try:
    while no<=limit:#finding the cube upto the user specified limit
      sq=no*no*no
      dict[no]=sq
      no+=1
    print dict 
  except:
    print "error"
limit=int(raw_input("enter the number"))
fun(limit)
test()