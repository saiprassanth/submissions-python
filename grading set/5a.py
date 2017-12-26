'''square upto the specified limit
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
  try:
    while no<=limit:#finding the square of the number upto the user specified limit
      sq=no*no
      print no,"squared is",sq
      no+=1#incrementing the number
  except:
    print "error"
limit=int(raw_input("enter the number"))
fun(limit)
test()