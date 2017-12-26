'''print date in a specified format
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is a test function",fun('2017 1 23')
  print "this is a test function",fun('2017 01 23')
def fun(date):
  dict={'01':'january','02':'february','03':'march','04':'april','05':'may','06':'june','07':'july','08':'august','09':'september','10':'october','11':'november','12':'december'}#declaring a dictionary for month number and corresponding month name
  l=date.split(" ")#converting the input into a list
  try:
    print l[2],"th",dict[l[1]],l[0]#printing the date in the specified format
  except:
    print "date format error"
date=raw_input("enter the date in year month and day format")
fun(date)
test()