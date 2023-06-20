#!/usr/bin/env python
# coding: utf-8

import math
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        return(val)
    except ValueError:
        print("No.. input is not a number. It's a string")

V = input("Enter in the valid number of votes ")
v = check_user_input(V)
S = input("Enter in the number of seats to allocate ")
s = check_user_input(S)
Q =(v/s+1)
print("the Quota is ",Q) 
