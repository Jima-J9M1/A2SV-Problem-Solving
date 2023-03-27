class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        def quickSort(num):
            if len(num) <= 1:
                return num
            
            pivot = num[0]
            left = []
            right = []
            
            for i in range(1, len(num)):
                if num[i] > pivot:
                    right.append(num[i])
                else:
                    left.append(num[i])
                    
            return quickSort(left) + [pivot] + quickSort(right)
        
        arr = quickSort(nums)
        ans = []
        
        count = 1
        
        while arr[0] - count > 0:
            ans.append(count)
            count += 1
            
        for i in range(1, len(arr)):
            val = arr[i - 1]
            val2 = arr[i]
            
            while val2 - val > 1:
                val += 1
                ans.append(val)
            
            while ( i == len(arr) - 1 and len(arr) - val2 > 0):
                val2 += 1
                ans.append(val2)
            
            
        
        return ans