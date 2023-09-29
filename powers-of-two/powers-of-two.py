collections import deque
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def bit_map(num1, k):
    bit_rep = bin(num1)
    bit_num = bit_count(num1)
    arr = [int(bit_rep[x]) for x in range(2,len(bit_rep))]
   
    ptr = 0
    if k < bit_num or k > num1:
      print("NO")
      return
    
    add = sum(arr)
    
    while add < k:
      if arr[ptr] > 0:
          arr[ptr] -= 1
          arr[ptr + 1] += 2
          add += 1
      else:
          ptr += 1
          
    
    res = arr[::-1]
    ans = []
    
    for indx in range(len(res)):
        if res[indx] > 0:
            
            for i in range(res[indx]):
                ans.append(2**indx)
 
    print("YES")
    print(*ans)
   
  
def bit_count(n):
    num1 = n
    i = 1
    count = 0
    
    while num1:
        if num1 & i > 0:
            count += 1
            
        num1 >>= 1
    
    return count
    
num1, num2 = MI()
 
bit_map(num1,num2)
    
