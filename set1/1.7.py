'''program to find if one string is in the other

saiprassanth.ramesh@accenture.com

02dec2017'''

def isin(s1,s2):

  if s2 in s1:

    print True

  else:

    print False

s1=raw_input('enter the first string')

s2=raw_input('enter the second string')

isin(s1,s2)