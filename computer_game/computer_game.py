from collections import deque, defaultdict
import math
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def ILI(list_val): return [x for x in list_val]
def LSI(): return list(map(str,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
 
def isbound(grid, row, col):
    return ((0 <= row < 2) and (0 <= col < len(grid[0])))
 
def solve():
    len_col = II()
    directions = [[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[-1,1],[1,-1],[1,1]]
    queue = deque([[0,0]])
 
    grid = []
    for __ in range(2):
        input_val = input()
        grid.append(ILI(input_val))
    
    grid[0][0] = 1
    while queue:
        len_level = len(queue)
        # print(queue)
        for _ in range(len_level):
 
            row, col = queue.popleft()
            
            if row == 1 and col == len_col - 1:
                print("YES")
                return
            
 
            for new_row, new_col in directions:
                new_row += row
                new_col += col
                if isbound(grid, new_row, new_col) and grid[new_row][new_col] == '0':
                    queue.append([new_row, new_col])
                    grid[new_row][new_col] = 1
 
    
    print("NO")
     
 
tastCase = II()
 
for _ in range(tastCase):
    solve()
