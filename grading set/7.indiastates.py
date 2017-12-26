'''pattern matching
saiprassanth.ramesh@accenture.com
'''
def test():
  #test function
  print "this is a test function",fun("Modernmedia saiprassanth dinesh tou Media visa pizza modern")
def fun(states):
  try:
    list=states.split(" ")
    res=False
    stateslist=["","","","",""]
    for i in list:
      #ends with esh
      if i.endswith("esh"):
        stateslist[0]=i  
    for i in list:
      #begins with t and ends with u
      if i.startswith("T")or i.startswith("t") and i.endswith("u"):
        stateslist[1]=i 
    for i in list:
      #begins with M and ends with a
      if i.startswith("M") and i.endswith("a"):
        stateslist[2]=i      
    for i in list:
      #ends with a
      if i.endswith("a"):
        stateslist[3]+=i+" "#adding the strings within the same element of the list   
    for i in list:
      #startes with M in the begning of the list
      if i==list[0]:
        if i.startswith("M")or i.startswith("m"):
          stateslist[4]=i
    print stateslist
  except:
    print "error"
states="Maharashtra Assam TamilNadu MadhyaPradesh Karnataka"
fun(states)
test()