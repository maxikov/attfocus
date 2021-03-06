#!/usr/bin/env python

import featurebuilder
import numpy
import numpy.linalg


def load_data(filename):
	src = open(filename, "r")
	X, Y = eval(src.readline())
	src.close()
	return X, Y

def solve_theta(X, Y):
	print "Stage 1 of 5:	theta = numpy.transpose(X)"
	theta = numpy.transpose(X)
	print "Stage 2 of 5: 	theta = numpy.dot(theta, X)"
	theta = numpy.dot(theta, X)
	print "Stage 3 of 5: 	theta = numpy.linalg.pinv(theta)"
	theta = numpy.linalg.pinv(theta)
	print "Stage 4 of 5: 	theta = numpy.dot(theta, numpy.transpose(X))"
	theta = numpy.dot(theta, numpy.transpose(X))
	print "stage 5 of 5: 	theta = numpy.dot(theta, Y)"
	theta = numpy.dot(theta, Y)
	return theta

def write_theta(theta):
	f = open("theta.py", "w")
	f.write(str(theta.tolist()))
	f.close()

def main():
	print "Loading data..."
	X, Y = load_data("../training_set.py")
	print "len(X):", len(X), "len(X[0]):", len(X[0]), "len(Y):", len(Y)
	print "Building features..."
	X = featurebuilder.build_nth_x_from_set(X)
	print "Size of X:", X.shape
	Y = featurebuilder.build_y(Y)
	print "Size of Y:", Y.shape
	print "Calculating theta..."
	theta = solve_theta(X, Y)
	print "Writing theta..."
	write_theta(theta)


if __name__ == "__main__":
	main()
