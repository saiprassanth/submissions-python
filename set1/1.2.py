'''program to print string with 70 spaces

saiprassanth.ramesh@accenture.com

02dec2017'''

def right_justify(s):

    return ' ' * (70 - len(s)) + s

s=raw_input('enter the string')

spa=right_justify(s)

print spa