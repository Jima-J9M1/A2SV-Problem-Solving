class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def rec(nums):
            if len(nums) == 1:
                return nums
            
            res = []
            for i in range(len(nums) - 1):
                cal = nums[i] + nums[i + 1]
                if cal > 9:
                    res.append(int(str(cal)[1]))
                else:
                    res.append(cal)
                    
            ans = rec(res)
            
            return ans
        
        result = rec(nums)
        
        return result[-1]
                