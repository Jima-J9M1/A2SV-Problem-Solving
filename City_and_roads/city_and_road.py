n = int(input())
count = 0

for __ in range(n):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
    
print(count // 2)
