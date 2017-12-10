'''program to print asterick pyramid using recursive and non recursive functions
saiprassanth
10dec2017'''
def nonrecursive():
  print "non-recursive"
  i=1
  j=7
  while i<=7:
    '''printing the pattern using non-recursive function'''
    if i!=4:
      print((j*' ')+i*'**')
    j=j-1
    i=i+1
def recursion(i=7,j=1):
  '''printing the pattern using recursive function'''
  if i> 1 :
    recursion(i-1,j+1)
  if i!=4:
    print(j*' '+'**'*i)
print "recursive"
recursion()
nonrecursive()