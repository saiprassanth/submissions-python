'''one to three line block of code
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is a test for function fun1",fun1("english")
  print "this is a test for function fun1",fun1("")
  print "this is a test for function fun2",fun2(0,0)
  print "this is a test for function fun2",fun2(-50,0)
  print "this is a test for function fun2",fun2(0,5)
  print "this is a test for function fun3",fun3(4)
  print "this is a test for function fun3",fun3(3)
def fun1(string):
  #printing string with 50 ! marks
  try:
    string+="!"*50
  except:
    print "error"
  print string 
def fun2(i,n):  
  #printing even numbers from 0 too 100
  try:
    while i<=n:
      if i%2==0:
        print i
      i+=1
  except:
    print "error"
def fun3(n):
  #checking if the use entered values is odd
  try:
    if n%2!=0:
      print "Entry validated"
  except:
    print "error"
string="sai"
fun1(string)
fun2(0,100)
n=int(raw_input("enter the number"))
fun3(n)
test()