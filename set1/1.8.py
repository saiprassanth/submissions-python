'''ratio between two lists
saiprassanth.ramesh@accenture.com
4dec2017'''
def ratio(vect1, vect2):
  ratios=[]
  try:
    for i in range(len(vect1)):
      listitem1=vect1[i]
      listitem2=vect2[i]
      ratios.append(listitem1/listitem2)
    return ratios
  except IndexError:
    print "enter lists with same size"
str1=raw_input('enter the first list')
str2=raw_input('enter the second list')
vect1=[]
vect2=[]
for i in str1:
  try:
    j=float(i)
    vect1.append(j)
  except ValueError:
    pass
for i in str2:
  try:
    j=float(i)
    vect2.append(j)
  except ValueError:
    pass
c=ratio(vect1,vect2)
print c