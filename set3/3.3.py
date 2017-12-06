'''to find e in string
saiprassanth.ramesh@accenture.com
5dec2017'''
def has_no_e(str):  
  if 'e'  in str:
    print False
  elif 'E' in str:
    print False
  else:
    print True
str=raw_input('enter the string')
has_no_e(str)