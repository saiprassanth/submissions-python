'''number rotation
saiprassanth.ramesh@accenture.com
5dec2017'''
def rotate_word(str,rot):
  asc=[]
  rotated=[]
  final=[]
  for i in str:
    asc.append(ord(i))
  for i in asc:
    i+=rot
    rotated.append(i)
  for i in rotated:
    final.append(chr(i))
  print "".join(final)
str=list(raw_input('enter the string'))
rot=int(raw_input('enter the distance you want to rotate'))
rotate_word(str,rot)