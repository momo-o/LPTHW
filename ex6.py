x="There are %d types of people." %10 #设置变量 with 格式化字符
binary="binary" #设置变量
do_not="don't" #设置变量
y="Those who know %s and those who %s." %(binary,do_not) #设置变量 with 格式化字符

print x #打印带有格式化字符的变量
print y

print "I said:%r." %x #这里的格式化字符本身就带有格式化字符，两层；用的%r，会打印引号
print "I also said:'%s'." %y #同上但用的是%s，只打印字符串

hilarious = False
joke_evaluation="Isn't that joke so funny? %r "

print joke_evaluation %hilarious #格式化字符与后面的字符串可以通过两个变量来分别实现。

w = "This is the left side of..."
e = "a string with a right side."

print w+e