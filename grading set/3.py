'''linear search algorithm
saiprassanth.ramesh@accenture.com
'''
def test():
  #this is a test functiom
  print "thi is a test function\n",fun(['a','s','1','2'],'a')
  print "thi is a test function\n",fun(['a','s','1','2'],'2')
  print "thi is a test function\n",fun(['a','s','1','2'],'6')
def fun(list,search):
  count=0
  flag=False
  for i in list:
    #linear search
    count+=1#count to keep track of the number of searches
    try:  
      if i==search:
        flag=True
        break
      else:
        continue
    except:
      print "error"
  if flag==True:
    print "element is present in the list"
  else:
    print "element is not present in the list"
    list.append(search)#appending the element if it is not in the list
    print "element added to the list",list
  print "number of searches performed are",count
str=raw_input("enter the elements seperates by comma")
list=str.split(",")
search=raw_input("enter the element to be searched") 
fun(list,search)
test()