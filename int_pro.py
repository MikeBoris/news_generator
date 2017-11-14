# eg program with int
import sys
N = int(sys.argv[1])
xnm1 = 1
xnm2 = 1
n = 2
while n <= N:
	xn = xnm1 + xnm2
	print('x_{0}= {1}'.format(n, xn))
	xnm2 = xnm1
	xnm1 = xn
	n += 1