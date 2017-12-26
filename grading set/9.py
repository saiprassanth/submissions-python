'''seperating the even elements from the list
saiprassanth.ramesh@accenture.com
'''
def test():
  #this is a test function
  print "this is a test function",fun("2,4,6,8,10")
  print "this is a test function",fun("1,3,5,7,9")
  print "this is a test function",fun("0,0,0,0,0")
def fun(str):
  try:
    list=str.split(",")#conveting the string to a list
    lis=[i for i in list if int(i)%2!=0]#using list comprehension to add the odd elements in a new list
    return ",".join(lis)
  except:
    print "error in the input"
str=raw_input("enter the sequence of numbers seperated by commas")
print fun(str)
test()