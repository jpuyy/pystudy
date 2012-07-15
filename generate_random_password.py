#!/usr/bin/env python
# -- coding: utf-8 --
# this script using for generate random password

import random
import string
 
def render(len=8, num_flag=True, low_flag=True, up_flag=True, special_flag=True):
	num = "0123456789"
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special = "~!@#$%^&*()[]{}_=+-"
 
	str = ''
	if num_flag:
		str += num
	if low_flag:
		str += lower
	if up_flag:
		str += upper
	if special_flag:
		str += special
	if str == '':
		str = num + lower
	return string.join(random.sample(str, len)).replace(" ", "")
 
	if __name__ == '__main__':
 
		i = 0
		while(i < 10):
			print render()
			i += 1
a_random_password = render()
print "a password is: %r" % a_random_password
