'''a is power of b if divisible by b a/b is power of b

saiprassanth.ramesh@accenture.com

03dec2017'''

def is_power(a,b):

  if a==b:

    return True

  elif a%b==0:

    return is_power(a/b,b)

  else:

    print 'not divisible'

    return False

a=int(raw_input('enter the first number'))

b=int(raw_input('enter the second number'))

print is_power(a,b)

