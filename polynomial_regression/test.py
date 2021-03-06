#!/usr/bin/env python

import featurebuilder
import numpy


def load_data(filename):
	src = open(filename, "r")
	X, Y = eval(src.readline())
	src.close()
	return X, Y

def load_theta(filename):
	src = open(filename, "r")
	theta = eval(src.readline())
	src.close()
	return theta


def main():
	print "Loading data..."
	X, Y = load_data("../test_set.py")
	print "len(X):", len(X), "len(X[0]):", len(X[0])
	print "Building features..."
	X = featurebuilder.build_nth_x_from_set(X)
	print "Size of X:", X.shape
	Y = featurebuilder.build_y(Y)
	print "Size of Y:", Y.shape
	print "Loading theta..."
	theta = load_theta("theta.py")
	print "Testing..."
	Y_estimate = numpy.dot(X, theta)
	for i in xrange(Y.size):
		print "Estimate:", Y_estimate[i], "Real:", Y[i]
	diff = Y_estimate - Y
	print "Average difference between estimate and real:", sum(abs(diff))/diff.size
	errors = 0
	for i in xrange(Y_estimate.size):
		est = numpy.round(Y_estimate[i][0])
		act = Y[i][0]
		if est != act:
			errors += 1
	print "Errors:", errors
	print "Error percentage:",   100*float(errors)/float(Y.size)




if __name__ == "__main__":
	main()
