'''first even in the list

saiprassanth.ramesh@accenture.com

03dec2017'''

def first_even(l):

  for i in l:

    if i%2 == 0:

      return i

s=raw_input('enter the list of numbers')

l=[]

for i in s:

  try:

    l.append(int(i))

  except ValueError:

    pass

if first_even(l):

  print 'the first even is',first_even(l)

else:

  raise ValueError('no even numbers')
