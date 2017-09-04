#! python

import sys

input = input("What is your name?\n")
sys.stdout.write("hello from Python, %s!\n" % (input))
print("hello ",end='')
print("world")