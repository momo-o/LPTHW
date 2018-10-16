# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(5,0) 
#这里的seek函数中后一个参数代表指针定位处，0是文档最前面，1是当前位置，2是文档最末；前一个参数代表与指针定位处的便宜的字符数，正是往后，负是往前。

def print_a_line(line_count,f):
	print line_count,f.readline()

current_file = open(input_file)

print "First let's print the whoele file:\n"
print_all(current_file)

print "Now lets rewind,kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line=1
print_a_line(current_line, current_file)

current_line+=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)
