#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    isSwapped=0
    temp=0
    count=0
    for i in range(len(a)):
        for j in range(0,n-(i+1)):
            if a[j]>a[j+1]:
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
                    isSwapped=1
            else:
                isSwapped=0
            if isSwapped==1:
                count+=1
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")



    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
