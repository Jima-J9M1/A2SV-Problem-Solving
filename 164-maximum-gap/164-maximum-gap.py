class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        
        def insertionSort(num):
            ptr = 0
            
            for indx in range(1, len(num)):
                val = num[indx]
                
                while ptr >= 0 and val < num[ptr]:
                    
                    num[ptr + 1] = num[ptr]
                    ptr -= 1
                    
                num[ptr + 1] = val
                ptr = indx
                
            
            return num
        
        
        
        
        def bucketSort(num):
            min_val = min(num)
            max_val = max(num)
            bucket =[[]  for __ in range(1000)]
            ans = []
            rang = max_val  - min_val
            
            if rang == 0:
                return num
            
            for i in range(len(num)):
                bucket[ 999 * (num[i] - min_val) // rang].append(num[i])
                # print(bucket[999 * (num[i] - min_val) // rang])
            
            for ele in bucket:
                ans.extend(insertionSort(ele))
                
            return ans
        
        sorted_val = bucketSort(nums)
        
        max_difference_val = float("-inf")
        
        for i in range(1, len(sorted_val)):
            max_difference_val = max(max_difference_val, sorted_val[i] - sorted_val[i - 1])
            
        return max_difference_val if max_difference_val != float("-inf") else 0