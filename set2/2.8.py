'''eval function

saiprassanth.ramesh@accenture.com

03dec2017'''
import math
def eval_loop():

  while True:

    res=''

    str=raw_input('enter the string')

    if str=='done':

      break

    else:

      res=eval(str)

      print res

  print res

eval_loop()
