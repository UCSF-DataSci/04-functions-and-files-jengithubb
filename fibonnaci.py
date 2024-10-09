#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def gen_fib(limit):
	left = 0
	right = 1
	tem = 0
	fib_list = []
	while left + right < limit:
		if(len(fib_list) == 0):
			fib_list.append(left)
			fib_list.append(right)
			
		tem = right
		right = left+right
		left = tem
		fib_list.append(right)
	return fib_list

if __name__ == "__main__":  
	parser = argparse.ArgumentParser()
	parser.add_argument('upper_limit', type = int, help ='upper limit for the fibonacci number')
	parser.add_argument('output_file_name', type = str, help = 'output file name')
	args = parser.parse_args()
	print(f"The upper limit is {args.upper_limit}")
	print(f"The output file is {args.output_file_name}")

	try :
		with open( args.output_file_name, 'r+') as hey:
			hey.write(','.join(map(str, gen_fib(args.upper_limit))))

	except FileNotFoundError:
		print(f"Error: File '{args.output_file_name}' not found.")

	