'''program to find if the string is palindrome or not without using the step size
saiprassanth.ramesh@accenture.com
8dec2017'''
def palindrome(str):
  '''function to return the reverse of the given string'''
 
  length=len(str)
  length-=1
  rev=[]
  while length>=0:
    '''reading the elements in the reverse order and appending them to a list'''
    element=str[length]
    rev.append(element)
    length-=1
  strre="".join(rev)
  '''converting the list into a string'''
  if str==strre:
    '''checking if the reversed string and original string are the same'''
    return "palindrome"
  else:
    return "not a palindrome" 
def test():
  print "--------------------it is a test function--------------------"
  print "noon\t",palindrome('noon'),"\texpected result is 'palindrome'"
  print "palindrome\t",palindrome('palindrome'),"\texpected result is 'not a palindrome'"
str=raw_input('enter the input')
'''receiving the input from the user'''
print palindrome(str)
test()