'''program to find if the list is sorted or Not



saiprassanth.ramesh@accenture.com



5dec2017'''



def is_sorted(list1):

  
  sort=sorted(list1)

  
  if "".join(list1)=="".join(sort):

    return True

  else:

    return False




str=raw_input("enter string seperated by comma")


list1=str.split(',')



print is_sorted(list1)