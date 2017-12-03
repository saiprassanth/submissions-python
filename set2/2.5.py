'''sum of digits in string

saiprassanth.ramesh@accenture.com

03dec2017'''

def digitsum(s):
 
  total = 0

  for i in s:

    try:

      total += int(i)

    except ValueError:

      pass
  
  print total

s=raw_input('enter the string')

digitsum(s)
