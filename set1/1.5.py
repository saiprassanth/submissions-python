'''root and power pairs

saiprassanth.ramesh@accenture.com

02dec2017'''

num=int(raw_input('enter the number'))

base=1

power=2

flag=False

while power<6:

  while base**power<=num:

    if base**power==num:

      print 'the base is ',base

      print 'the power is ',power

      flag=True

    base+=1

  power+=1

  base=1

if flag==False:

  print 'no such combination exists'