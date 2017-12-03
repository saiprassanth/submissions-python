'''program to find the largest odd
 among three
saiprassanth.ramesh@accenture.com


02dec2017'''

a = int(raw_input('Enter your first integer: '))

b = int(raw_input('Enter your second integer: '))

c = int(raw_input('Enter your third integer: '))

largest = max(a%2*a, b%2*b, c%2*c)

if largest == 0:

    print 'There are no odd numbers'

else:
 
   print 'is the largest odd integer',largest