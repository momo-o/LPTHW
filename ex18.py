def print_two(*args): #define function name and the name and number of arguments.
	arg1,arg2 = args
	print "arg1:%r, arg2=%r" %(arg1,arg2) #operate with arguments and present the outcome.

def print_two_again(arg1,arg2):
	print "arg1:%r, arg2=%r" %(arg1,arg2)

def print_one(factor):
	print "arg1: %r" %factor

def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First")
print_none()