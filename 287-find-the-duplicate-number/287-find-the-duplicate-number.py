class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Binary Search"""
        
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        
        while right - left > 1:
            count = 0
            
            for num in nums:
                if mid < num <= right:
                    count += 1
                    
            if count > right - mid:
                left = mid
            else:
                right = mid
            
            mid = left + (right - left ) // 2
        
        return right
        
        
        
        """ans = 0
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans = abs(num)
            
            else:
                nums[abs(num) - 1] *= -1
                
        return ans"""