class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference_arr = []
        
        for left, right in costs:
            diff = left - right
            
            difference_arr.append([diff, left, right])
        
        sorted_arr = self.pivotSort(difference_arr)
        
        comp_a = 0
        comp_b = 0
        check = True
        for indx in range(len(sorted_arr)//2):
            comp_a += sorted_arr[indx][1]
            
        for indx in range(len(sorted_arr)//2, len(sorted_arr)):
            comp_b += sorted_arr[indx][2]
        
        
        return comp_a + comp_b
          
            
            
            
        
        
        
    def pivotSort(self,nums):
        if len(nums) <= 1:
            return nums
        
        pivot = nums[0]
        left = []
        right = []
        
        for i in range(1, len(nums)):
            if nums[i] > pivot:
                right.append(nums[i])
            else:
                left.append(nums[i])
                
                
        return self.pivotSort(left) + [pivot] + self.pivotSort(right)