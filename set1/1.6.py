'''sum of decimal numbers

saiprassanth.ramesh@accenture.com

02dec2017'''

s=raw_input('enter the list of decimal numbers')

total=0

snum=s.split(',')

for i in snum:

  n=float(i)

  total=total+n

print total