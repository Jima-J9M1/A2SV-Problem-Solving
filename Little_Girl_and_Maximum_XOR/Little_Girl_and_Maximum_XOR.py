collections import deque
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def bit_map(num1, num2):
   if num1 == num2:
       print(0)
       return
   
   num_length = int.bit_length(num1)
   num2_length = int.bit_length(num2)
   
   if num_length < num2_length:
       shift_bit = 1 << num2_length - 1
       print(shift_bit ^ (shift_bit - 1))
       return 
   
   xor_val = num2 ^ num1
   bit_len = int.bit_length(xor_val)
   ans  = 1 << bit_len
   
   print(ans - 1)
   
num1, num2 = MI()
bit_map(num1, num2)
 
    
 
    
