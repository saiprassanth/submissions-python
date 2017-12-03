'''GCD

saiprassanth.ramesh@accenture.com

03dec2017'''

def GCD(a,b):

  if b==0:

    return a

  else:

    r=a%b

    return GCD(b,r)

a=int(raw_input('enter the first number'))

b=int(raw_input('enter the second number'))

print GCD(a,b)