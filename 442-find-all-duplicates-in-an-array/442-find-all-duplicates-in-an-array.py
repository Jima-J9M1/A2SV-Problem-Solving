class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        ans = []
        def quickSort(num):
            if len(num) <= 1:
                return num
            
            
            pivot = num[0]
            left = []
            right = []
            
            for idx in range(1, len(num)):
                
                if num[idx] > pivot:
                    left.append(num[idx])
                elif num[idx] < pivot:
                    
                    right.append(num[idx])
                else:
                    ans.append(num[idx])
                    
            return quickSort(left) + [pivot] + quickSort(right)
        
        num = quickSort(nums)
        
        return ans
        '''
        res = []
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        
        return res
           

                    
                        
                        
                        