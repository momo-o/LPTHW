# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

txt = open(filename) #这里的打开是在后台打开

print "Here's your file %r:" %filename
print txt.read() #打开后读取的内容才可以打印

txt.close()

print "Type the filename again:"#这是另一种打开文本文件方式
file_again = raw_input(">")#把文本文件名赋给一个变量，这样也方便打开另外的文本文件

txt_again=open(file_again)

print txt_again.read()
txt.close()

