'''program to check if there is a forbidden string within the main string

saiprassanth.ramesh@accenture.com

5dec2017'''

def avoids(str1,forb):

  if set(str1) & set(forb):

    return False

  else:

    return True

str1=list(raw_input("enter the string"))

forb=list(raw_input("enter the forbidden string"))

res=avoids(str1,forb)

print res