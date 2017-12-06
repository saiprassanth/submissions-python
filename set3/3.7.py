'''program to find if the list contains only the specified alphabets


saiprassanth.ramesh@accenture.com


5dec2017'''


def using_only(str,letters):


  tmp=0


  s=set(str)


  for i in letters:


    if i in str:


      tmp+=1

 
  if tmp==(len(s)):


   return True


  else:


    return False


str=raw_input('enter the word')


str1=raw_input('enter the letters seperated by comma')


letters=str1.split(',')


res=using_only(str,letters)


print res