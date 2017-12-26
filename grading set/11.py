'''matrix multiplication using files
saiprassanth.ramesh@accenture.com
'''
def test():
  #this is a test function
  print "this is a test function"
  file=open('a.txt','w')#creating a new file
  file.write("x:\t-1\t0\t3\t64")#writing the necessary contents into the file
  file.close()
  file1=open('b.txt','w')
  file1.write("z:\t0\t2\t4\t-4")
  file1.close()
  file=open('a.txt','r')#opening already existing file
  file1=open('b.txt','r')
  fun(file,file1)
def fun(file,file1):
  try:
    lis=file.readline()#reading the contents of the file and storing it in a variable
    a=lis.split('\t')#converting the string read from file into a list
    del a[0]#deleting the initial string part in the list
    x=[int(i) for i in a]#converting the string list into an integer list
    print "x is",x
    y=[2*i for i in x ]#calculating Y=2*X
    print "y is 2 * x which is equal to",y
    lis1=file1.readline()
    b=lis1.split('\t')
    del b[0]
    z=[int(i) for i in b]
    print "z is ",z
    y=[x[i]*z[i] for i in range(len(x))]#calculating Y=X*Z
    print "product of x and z is",y
  except:
    print "error"
try:
  file=open('1.txt','w')#creating a new file
  file.write("x:\t1\t2\t3\t4")#writing the necessary contents into the file
  file.close()
  file1=open('2.txt','w')
  file1.write("z:\t1\t2\t4\t4")
  file1.close()
  file=open('1.txt','r')#opening already existing file
  file1=open('2.txt','r')
  fun(file,file1)
  test()
except:
  print "error"