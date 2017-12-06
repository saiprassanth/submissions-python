'''program to check abecedarian words

saiprassanth.ramesh@accenture.com

5dec2017'''

def is_abecedarian(str):
    if str == "".join(sorted(str)):
      print True
    else:
      print False
str=raw_input('enter the word')
is_abecedarian(str)