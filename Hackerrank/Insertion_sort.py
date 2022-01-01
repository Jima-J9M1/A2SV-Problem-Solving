#!/bin/python3

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
    l=len(arr)
    b=""
    j=l-2
    value=arr[l-1]
    while j>=0 and value<arr[j]:
        arr[j+1]=arr[j]
        j-=1
        b=str(arr)[1:-1].replace(",", "")
        print(b)

    arr[j+1]=value
    b=str(arr)[1:-1].replace(",", "")
    print(b)


    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
