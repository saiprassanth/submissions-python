'''to find e in a list  of strings and return the string without e and percent of strings without e
saiprassanth.ramesh@accenture.com
5dec2017'''
str=raw_input('enter the  list of strings with comma')
strlist=str.split(',')
olength=float(len(strlist))
wo_e=[]
wi_e=[]
for str in strlist:
  if 'e' in str:
    wi_e.append(str)
  elif 'E' in str:
    wi_e.append(str)
  else:
    wo_e.append(str)
print wo_e
elength=len(wo_e)
percent=(elength/olength)*100
print 'percent without e is ',percent