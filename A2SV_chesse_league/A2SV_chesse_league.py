from collections import deque, Counter, defaultdict
import math


def II(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def SI(): return sorted(list(map(int, input().split())))


def merge(a1, a2, k):
    l1 = l2 = 0
    new_arr = []

    while l1 < len(a1) or l2 < len(a2):
        num1, idx1 = a1[l1] if l1 < len(a1) else (float('inf'), idx1)
        num2, idx2 = a2[l2] if l2 < len(a2) else (float('inf'), idx2)
        if num1 <= num2:
            if a2[0][0] - k <= num1: new_arr.append(tuple([num1, idx1]))
            l1 += 1
        else:
            if a1[0][0] - k <= num2: new_arr.append(tuple([num2, idx2]))
            l2 += 1

    return new_arr


def mergeSort(left, right, arr, diff):
    if left == right:
        return [arr[left]]

    mid = left + (right - left) // 2

    left = mergeSort(left, mid, arr, diff)
    right = mergeSort(mid + 1, right, arr, diff)

    return merge(left, right, diff)


def solve():
    rounds, diff = MI()
    matches = LI()
    chessLeague = [(match, indx + 1) for indx, match in enumerate(matches)]

    ans = mergeSort(0, (2**rounds) - 1, chessLeague, diff)

    sorted_val = [x[1] for x in sorted(ans, key=lambda x: x[1])]
    print(*sorted_val)


solve()
