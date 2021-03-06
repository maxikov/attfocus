import numpy
import math
import itertools



def nth_arr_from_sample(sample, n=4):
	res = map(lambda x: reduce(lambda a, b: a*b, x, 1), itertools.combinations_with_replacement(sample, n))
	return res

def build_nth_x_from_set(arr_X, n = 6):
	l = len(arr_X)
	order = len(arr_X[0]*n)
	print "Original features:", len(arr_X[0])
	print "Built features:", order
	X = None
	for i in xrange(len(arr_X)):
		sample = arr_X[i]
		res = []	
		for x in sample:
			for i in xrange(1,n+1):
				y = x**i
				res.append(y)
				if numpy.isnan(y) or numpy.isinf(y):
					print "{}**{} = {}".format(x, i, y)
		arr_res = numpy.array(res, dtype="float64")
		arr_res = arr_res.reshape([1, arr_res.size])
		if X == None:
			X = arr_res
		else:
			X = numpy.vstack( (X, arr_res) )
	return X	

def build_y(arr_Y):
	res = numpy.array(arr_Y, dtype="float64")
	return res
