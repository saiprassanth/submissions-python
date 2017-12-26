'''no of occurrences of an alphabet in the string
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is a test function\n",fun("abcdefg")
  print "this is a test function\n",fun("aaaaaaa")
def fun(str):
  dic={}
  try:
    for x in str:
      dic[x]=str.count(x)#storing the key and its count in the dictionary
    for x in dic:
      print"{},{}".format(x,dic[x])#printing the elements of the dictionary line by line
  except:
    print "error"
str=raw_input("enter the string")
fun(str)
test()