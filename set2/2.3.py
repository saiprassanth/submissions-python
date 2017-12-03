
'''factorial using recursion and iteration

saiprassanth.ramesh@accenture.com

03dec2017'''


#using iteration



def facti(n):

  fact=1

  for i in range(1,n+1):

    fact=fact*i

  return fact

print facti(5)



#using recursion


def factr(n):

  if n==1:

    return 1

  else:

    return n*factr(n-1)

print factr(6)