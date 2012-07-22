#!/usr/bin/env python
# -- coding: utf-8 --
from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
		"Nice job, you died ...jackass.",
		"Such a loser.",
		"I have a small puppy that's better at this."]
	print quips[randint(0, len(quips)-1)]
	exit(1)

def central_corridor():
	print "The Gothons of Planet
