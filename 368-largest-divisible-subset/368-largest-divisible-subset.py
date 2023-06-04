class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        memo = {}
        
        def dp(indx):
            if indx == 0:
                return [nums[indx]]
            
            if indx in memo:
                return memo[indx]
            
            subset = []
            max_length = 0
            
            for i in range(indx):
                if nums[i] % nums[indx] == 0 or nums[indx] % nums[i] == 0:
                    res = dp(i)
                    n = len(res)
                    
                    if max_length < n:
                        max_length = n
                        subset = res[:]
                        
            subset += [nums[indx]]    
            memo[indx] = subset
            return memo[indx]
        
        
        max_length = 1
        nums.sort()
        for i in range(len(nums)):
            res = dp(i)
            n = len(res)
            if max_length <= n:
                ans = res[:]
                max_length = n
                
        print(memo) 
        return ans
                
        