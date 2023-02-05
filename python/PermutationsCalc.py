#!/usr/bin/env python
# coding: utf-8

import math
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")


# input values for n and r and calculate nPr    
N = input("Enter the number of candidates(n) > ")
check_user_input(N)
n= int(N)
R= input("Enter the number of preferences cast (r) > ")
check_user_input(R)
r=int(R)

if r <= n:
    print(n)
    print(r)
    perms = int((math.factorial(n)/(math.factorial(n-r))))
    print(perms)
else:
    print("r is bigger than n")


# input values for n and r and calculate nPr    
N = input("Enter the number of candidates(n) > ")
check_user_input(N)
n= int(N)

#Print all Permutations for n candidates
print("Print all Permutations for "+ str(n) + " candidates")
for r in range(1,n+1):
    perms = int((math.factorial(n)/(math.factorial(n-r))))
    print(r, perms)




