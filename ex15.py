#!/usr/bin/env python
# -- coding: utf-8 --

#从sys里加入变量argument avariale
from sys import argv


script, filename = argv

#打开名叫filename的文件
txt = open(filename)


print "Here's your file %r:" % filename

#把读取到的文字打印出来
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
