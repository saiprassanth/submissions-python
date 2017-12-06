'''palindrome using slice
saiprassanth.ramesh@accenture.com
5dec2017'''
def is_palindrome(str1):
  str2=str1[::-1]
  if str1==str2:
    print 'palindrome'
  else:
    print 'not a palindrome'
str1=raw_input('enter the string')
is_palindrome(str1)