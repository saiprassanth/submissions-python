'''palindrome

saiprassanth.ramesh@accenture.com

03dec2017'''

n=raw_input('enter the string')

l=[]

for i in n:

  if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':

    j=i.lower()

    l.append(j)

stri="".join(l)

strre=stri[::-1]

if stri==strre:

  print 'palindrome'

else:

  print 'not a palindrome' 