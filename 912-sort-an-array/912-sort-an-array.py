class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(num1, num2):
            ptr1 = 0
            ptr2 = 0
            ans = []
            
            while ptr1 < len(num1) and ptr2 < len(num2):
                
                if num1[ptr1] > num2[ptr2]:
                    ans.append(num2[ptr2])
                    ptr2 += 1
                    
                else:
                    ans.append(num1[ptr1])
                    ptr1 += 1
                    
                
            if ptr1 < len(num1):
                ans += num1[ptr1:]
                
            if ptr2 < len(num2):
                ans += num2[ptr2:]
                
                
            return ans
        
        
        def mergeSort(nums,left,right):
            if left == right:
                return [nums[left]]
            
            
            mid = left + (right - left) // 2
            
            left = mergeSort(nums,left, mid)
            right = mergeSort(nums, mid + 1, right)
            
            return merge(left, right)
        
        
        ans = mergeSort(nums,0, len(nums) - 1)
        
        return ans
            
            
            
            
            
            
            
            
            
            
            
            