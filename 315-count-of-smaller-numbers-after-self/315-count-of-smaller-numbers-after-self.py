class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_val =  self.mergeSort(nums, 0, len(nums) - 1)
        
        result = [0] * len(nums)
        
        for index in range(len(sorted_val)):
            pos = sorted_val[index][2]
            val = sorted_val[index][1]
            result[pos] = val
        
        return result
        
        
    def merge(self, left, right):
        ptr1 = 0
        ptr2 = 0
        res = []
        indices = []
        
        while ptr1 < len(left) and ptr2 < len(right):
            if left[ptr1][0] <= right[ptr2][0]:
                res.append((left[ptr1]))
                ptr1 += 1
                
                
            else:
                indices.append(ptr1)
                # while cur < len(left):
                #     left[cur][1] += 1
                #     cur += 1
                    
                res.append((right[ptr2]))
                ptr2 += 1
        
        result = [0] * len(left)
        for index in indices:
            result[index] += 1
        
        for index in range(1,len(result)):
            result[index] = result[index] + result[index - 1]
            
        for index in range(len(left)):
            left[index][1] += result[index]
            
        
        if ptr1 < len(left):
            res += left[ptr1:]
        
        if ptr2 < len(right):
            res += right[ptr2:]
            
        return res
    
    
    def mergeSort(self, nums, left, right):
        if left == right:
            return [[nums[left], 0,left]]
        
        mid = left + (right - left) // 2
        
        left = self.mergeSort(nums, left, mid)
        right = self.mergeSort(nums, mid + 1, right)
        
        return self.merge(left, right)
    
        