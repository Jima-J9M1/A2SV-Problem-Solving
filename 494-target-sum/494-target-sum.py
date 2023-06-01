class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        res = self.dp(0, 0, nums, target, memo)
        return res
    
    
    def dp(self, indx, state, nums, target, memo):
        if (indx, state) not in memo:
            if indx == len(nums):
                return int(state == target)

            first = self.dp(indx + 1, state + nums[indx],nums, target, memo)
            second = self.dp(indx + 1, state - nums[indx], nums, target, memo)


            memo[(indx,state)] = first + second
            
        return memo[(indx, state)]
        