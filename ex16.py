# -*- coding: utf-8 -*-
from sys import argv

script,filename = argv #写入文件名

print "We're going to erase %r. " %filename
print "If you don't want that, hit CRTL-C (^C)." #这里输出CRTL-C真的可以退出
print "If you do want that, hit RETURN." #回车表示继续，67两行的套路以后说不懂会用到

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate() #因为前面打开时使用了writing命令，这里不用对文档进行truncate也可以

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1+"\n"+line2+"\n"+line3+"\n") #在txt中这个并不是真正的\n，打开txt后它就执行换行命令

print "And finally, we close it."
target.close()#每次都别忘了关闭文档