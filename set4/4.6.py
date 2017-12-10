'''program to perform temperature conversions
saiprassanth
10dec2017'''
class temperature:
  """abstract class"""
  def __init__(self, temperature):
    pass
  def __str__(self):
  	pass
  def aboveFreezing(self):
    pass
  def convertToFahren(self):
    pass
  def convertToCelsius(self):
    pass
  def convertToKelvin(self):
    pass


class fahrenheit(temperature):
  def __init__(self, temperature):
    self.degree=temperature
  def __str__(self):
  	return self.degree,"degrees fahrenheit"
  def aboveFreezing(self):
    """finding if farenhiet is above freezing"""
    if self.degree>32:
      return True
    else:
      return False
  def convertToCelsius(self):
    """converting farenhiet to celsius"""
    cons=5/9.0
    return (self.degree-32)*cons
  def convertToKelvin(self):
    """converting farenhiet to kelvin"""
    cons=5/9.0
    return (self.degree+459.67)*cons


class celsius(temperature):
  def __init__(self, temperature):
    self.degree=temperature
  def __str__(self):
  	return self.degree,"degrees celsius"
  def aboveFreezing(self):
    """finding if celsius is above freezing"""
    if self.degree>0:
      return True
    else:
      return False
  def convertTofarenheit(self):
    """converting celsius to farenhiet"""
    cons=9/5.0
    return (self.degree*cons)+32
  def convertToKelvin(self):
    """converting celsius to kelvin"""
    return self.degree+273.15


class kelvin(temperature):
  def __init__(self, temperature):
    self.degree=temperature
  def __str__(self):
  	return self.degree,"degrees kelvin"
  def aboveFreezing(self):
    """finding if kelvin is above freezing"""
    if self.degree>273.15:
      return True
    else:
      return False
  def convertToCelsius(self):
    """converting kelvin to celcius"""
    return self.degree-273.15
  def convertTofarenheit(self):
    """converting kelvin to farenhiet"""
    cons=9/5.0
    return (self.degree*cons)-459.67


f=float(raw_input("enter the temperature in farenhiet"))
c=float(raw_input("enter the temperature in celcius"))
k=float(raw_input("enter the temperature in kelvin"))
o1=fahrenheit(f)
o2=celsius(c)
o3=kelvin(k)
print o1.__str__()
print o2.__str__()
print o3.__str__()
print "is farenhiet above freezing ",o1.aboveFreezing()
print "is celcius above freezing ",o2.aboveFreezing()
print "is kelvin above freezing ",o3.aboveFreezing()
print "farenheit in celsius ",o1.convertToCelsius()
print "farenheit in kelvin ",o1.convertToKelvin()
print "celsius in farenheit",o2.convertTofarenheit()
print "celcius in kelvin ",o2.convertToKelvin()
print "kelvin in farenheit ",o3.convertTofarenheit()
print "kelvin in celcius",o3.convertToCelsius()
