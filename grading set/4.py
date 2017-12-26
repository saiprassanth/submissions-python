'''password strength
saiprassanth.ramesh@accenture.com
'''
def test():
  #this is atest function
  print "this is a test function",fun(['Aass1@','As1$','AASD12$','asd123@@','ASDas@$','ASDasd123','A1$','a1$','Aa$','Aa1','12345@$#','ASD#$@$','ASD12345','asdfg@#$','asdfgh12345','ASDasd','aaaaaaaa','1111111','AAAAAAAA','#########','a'])
def fun(list):
  special=['@','#','$']
  smallcase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  number=['1','2','3','4','5','6','7','8','9','0']
  strngpass=[]
  try:
    for i in list:
      lflag=False
      uflag=False
      nflag=False
      sflag=False
      lenflag=False
      if len(i)>=6 and len(i)<=12:#checking for length
        lenflag=True
      for x in i:
        if x in smallcase:#checking for small case
          lflag=True
        if x in uppercase:#checking for upper case
          uflag=True
        if x in number:#checking for number
          nflag=True
        if x in special:#checking for special character
          sflag=True
      if lflag and uflag and sflag and nflag and lenflag:
        strngpass.append(i)#appending the satisfied password to a list
    print "the strong password is",strngpass
  except:
    print "error"
str=raw_input("enter a set of comma seperated passwords")
list=str.split(",")
fun(list)
test()