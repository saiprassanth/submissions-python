'''code snippet

saiprassanth.ramesh@accenture.com

02dec2017'''


'''What would the code above return if the statement x = 25 were replaced by x = -25?
answer :It would become an infinite loop'''

x = -25

epsilon = 0.01

numGuesses = 0

low = 0.0

high = max(1.0, x)

ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:

  print 'low =', low, 'high =', high, 'ans =', ans

  numGuesses += 1

  if ans**2 < x:

    low = ans

  else:

    high = ans

  ans = (high + low)/2.0

print 'numGuesses =', numGuesses

print ans, 'is close to square root of', x


'''cube root of negative and positive numbers
saiprassanth.ramesh@accenture.com
5dec2017'''
z=int(raw_input('enter the number for which cube root is to be found'))
x =abs(z)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 1
  if ans**3 < x:
    low = ans
  else:
    high = ans
  ans = (high + low)/2.0
print 'numGuesses =', numGuesses
if z<0:
  print '-',ans, 'is close to cube root of', x
else:
  print ans, 'is close to square root of', x
