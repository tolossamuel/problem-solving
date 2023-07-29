#!/bin/python3
# https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    small=arr[len(arr)-1]
    for i in range(n-1,0,-1):
        if (arr[i-1]>small):
            arr[i]=arr[i-1]
            
        else:
            arr[i]=small
            small=arr[i]
        for y in arr:
            print(y,end=" ")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
