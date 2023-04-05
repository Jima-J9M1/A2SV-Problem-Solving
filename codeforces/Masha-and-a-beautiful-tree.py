def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def mergeSort(arr, left, right):
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    
    half_left  = mergeSort(arr, left, mid)
    half_right = mergeSort(arr, mid + 1, right)
    
    return merge(half_left, half_right)
    
    
def merge(num1, num2):
    ptr1 = 0
    ptr2 = 0
    
    
    if num1[ptr1] > num2[ptr2]:
        num2.extend(num1)
        count[0] += 1
        return num2
    else:
        num1.extend(num2)
        return num1
 
 
 
tasecases = II()
 
for __ in range(tasecases):
    size = II()
    arr = LI()
    count = [0]
    ans_arr = mergeSort(arr, 0, len(arr) - 1)
    sort_arr = sorted(arr)
    if ans_arr == sort_arr:
        
        print(count[0])
        
    else:
        
        print(-1)
    
