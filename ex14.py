from sys import argv

script, user_name, age = argv
a = '>'

print "Hi %s, I'm the %s script."%(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?"%user_name
likes=raw_input(a)

print "Where do you live, %s?"%user_name
lives=raw_input(a)

print "What kind of computer do you have?"
computer=raw_input(a)

print "Do you want to go outside for fun when you are %s?" %age
fun=raw_input(">")

print'''
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
And you said %r about going outside for fun when you are %s.
'''%(likes,lives,computer,fun,age)