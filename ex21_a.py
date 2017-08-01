# -*- coding: utf-8 -*-
def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a + b
def subtract(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a - b
def multiply(a,b):
	print "MULTIPLYING %d * %d" %(a,b)
	return a * b
def divide(a,b):
	print "DIVIDING %d/%d" %(a,b)
	return a / b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide (100,2)

a = divide(iq,2)
b = multiply(weight,a)
c = subtract(height,b)
what = add(age,c)

print "That becomes:", what, "Can you do it by hand?"


print  2 + 2*6/3

def routine_cost(actime,meal):
	return meal + 2*actime/3

d=routine_cost(6,2)

print d