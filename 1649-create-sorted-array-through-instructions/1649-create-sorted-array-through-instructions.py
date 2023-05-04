class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ans = self.mergeSort(instructions, 0, len(instructions) - 1)
        res = 0
        for val, min_val, max_val in ans:
            res += min(min_val, max_val)
        
        return res % (10 **9 + 7)
            
            
    
    
    def merge(self,left, right):
        l = 0
        r = 0
        size1 = len(left)
        size2 = len(right)
        merge = []
        
        while l < size1 and r < size2:
            
        #append if the left is less than the right
            if left[l][0] < right[r][0]:
                merge.append(left[l])
                l += 1
                
                
        #update the right higher by the length of the left from the current postion to the end  and the lower by the length of the left from the beging to the current position.
            elif right[r][0] < left[l][0]:
                right[r][2] += size1 - l
                right[r][1] += l
                merge.append(right[r])
                r += 1

            else:
                
                # right and left are equal                
                val = left[l][0]
                ptr = l
                
                #update the left value without updating the lower and higher values                 
                while l < size1 and right[r][0] == left[l][0]:
                    merge.append(left[l])
                    l += 1
                
                #increment the higher value if there is greate element in the left than in the right and increament the lower in the first one.                
                while r < size2 and right[r][0] == val:
                    right[r][2] += size1 - l
                    right[r][1] += ptr
                    merge.append(right[r])
                    r += 1
                    
                    
                
        if l < size1:
            merge += left[l:]
        
        while r < size2:

            right[r][1] += l
                
            merge.append(right[r])
                
            r += 1
            
        return merge
                
    
    def mergeSort(self,nums, left, right):
        if left == right:
            return [[nums[left],0,0]]
        
        mid = left + (right - left) // 2
        
        half_left = self.mergeSort(nums, left, mid)
        half_right = self.mergeSort(nums, mid + 1, right)
        
        
        return self.merge(half_left, half_right)
            
            
                