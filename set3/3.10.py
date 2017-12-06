'''program to check anagrams
saiprassanth.ramesh@accenture.com
5dec2017'''
def is_anagram(str1, str2):
  sor_str1=sorted(str1)
  sor_str2= sorted(str2)
  if sor_str1==sor_str2:
    print True
  else:
    print False
str1=raw_input('enter the first string')
str2=raw_input('enter the second string')
is_anagram(str1, str2)