#!/usr/bin/python
import sys

# Implementation of FizzBuzz v1.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end".
    def run(self, end, out=sys.stdout):
        for i in range(1, end + 1):
	    print >> out, self.calc(i)

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
	if i % 15 == 0:
	  return "FizzBuzz"
	elif i % 3 == 0:
	  return "Fizz"
	elif i % 5 == 0:
	  return "Buzz"
	else:
	  return i

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
