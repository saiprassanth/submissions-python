'''program to find the largest odd
 among ten
saiprassanth.ramesh@accenture.com

02dec2017'''
a = int(raw_input('Enter your first integer: '))
b = int(raw_input('Enter your second integer: '))
c = int(raw_input('Enter your third integer: '))
d = int(raw_input('Enter your fourth integer: '))
e = int(raw_input('Enter your fifth integer: '))
f = int(raw_input('Enter your sixth integer: '))
g = int(raw_input('Enter your seventh integer: '))
h = int(raw_input('Enter your eighth integer: '))
i = int(raw_input('Enter your ninth integer: '))
j = int(raw_input('Enter your tenth integer: '))

largest = max(a%2*a, b%2*b, c%2*c, d%2*d, e%2*e, f%2*f, g%2*g, h%2*h, i%2*i, j%2*j)

if largest == 0:
    print 'There are no odd numbers'
else: 
    print 'is the largest odd integer',largest