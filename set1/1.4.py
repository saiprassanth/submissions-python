'''python interpreter as calculator

saiprassanth.ramesh@accenture.com

02dec2017'''

r = int(raw_input('Enter the radius of the sphere: '))

c=(4/3.0)

pi=3.14

cube=r**3

area=c*pi*cube

print 'the area is',area

coverprice=24.95

discount=40/100.0

shippingcost1=3

scost=0.75

count=60

discountprice=coverprice*discount

totalprice=(coverprice-discountprice)*count

total= totalprice+shippingcost1+(count-1)*scost

print 'price for 60 books',total

timelefthouse = 6 * 3600 + 52 *60

mileseasy = 2 * (8 * 60 + 15 )

milesfast = 3 * (7 * 60 + 12 )

totaltime = mileseasy + milesfast + timelefthouse

hours = totaltime/ 3600

remainingseconds= totaltime % 3600

minutes = remainingseconds /60

seconds = remainingseconds % 60

print 'Hours:',hours

print 'minutes:', minutes

print 'seconds:', seconds
