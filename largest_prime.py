#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
# You're on your own for this one. Good luck!

import argparse
import math
import fibonnaci


def f_prime(n):
	if n <= 1:
		return 0
	if n == 2:
		return 1
	if n > 2 and n%2 == 0:
		return 0
	divisor = 3
	while divisor <= math.sqrt(n):
		result = n/divisor
		if result.is_integer():
			return 0
		divisor +=1
	return 1	



if __name__ == "__main__":  
	parser = argparse.ArgumentParser()
	parser.add_argument('upper_limit', type = int, help ='upper limit for the fibonacci number')
	args = parser.parse_args()
	rlist = sorted(fibonnaci.gen_fib(args.upper_limit),reverse=True)
	for i in rlist:
		if f_prime(i) == 1:
			print(f"The largest prime number is {i}")
			break
	
