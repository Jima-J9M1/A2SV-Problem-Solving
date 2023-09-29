int(input())
def MI():return map(int, input().split())
def LI():return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI():return input()
def LSI():return list(input())
def LSI_():return [i for i in input().split()]
 
def prime_factorization(num1):
    
    shift = 0
    while num1 & 1 == 0:
        num1 = num1 >> 1
        shift += 1
    
    result_val = 1 << shift
    return (num1, result_val)
              
 
 
def main():
    length = II()
    arr = LI()
    ans = 1
    sum_result = 0
    max_val = 0
 
    for ele in arr:
        odd_val,factor_two = prime_factorization(ele)
        max_val = max(max_val, odd_val)
        ans *= factor_two
        sum_result += odd_val
    
    print(((ans * max_val) + sum_result) - max_val)
 
 
 
tasteCase = II()
for _ in range(tasteCase):
    main()
 
 
    
