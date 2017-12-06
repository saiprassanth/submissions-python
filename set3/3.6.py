'''program to check if there is a forbidden string within the list of main string

saiprassanth.ramesh@accenture.com

5dec2017'''

def avoids(str1,forb):

  count=0

  for i in str1:

    if set(i) & set(forb):

      print i,'contains',"".join(forb)

    else:

      print i,' does not contain',"".join(forb)

      count+=1

  print 'number of words thet does not contain the forbidden string is',count

str=raw_input("enter the list of strings seperated by comma")

str1=str.split(',')

forb=list(raw_input("enter the forbidden string"))

avoids(str1,forb)