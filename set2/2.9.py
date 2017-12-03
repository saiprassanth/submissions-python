'''newton sqrt

saiprassanth.ramesh@accenture.com

03dec2017'''

import math

def newtonsqrt(a):

	a = float(a)
	x = a / 2
	i = 0

	while i < 10:

		y = (x + a / x) / 2

		x = y

		i += 1

	return y

def matsqr(a):

	a = float(a)

	return math.sqrt(a)

def display():
	print '|{}|\t{:13}|\t{:13}|\t{:17}|'.format('number','newtonssqrt', 'math.sqr', 'difference')

	print '------------------------------------------------------------------'

	for i in range(1, 10):

		n = newtonsqrt(i)

		m = matsqr(i)

		ab = abs(n - m)
		print '|{:6}|\t{:13}|\t{:13}|\t{:17}|'.format(i,n, m, ab)

display()