class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        prefix_sum = [0] * (len(nums) + 1)
        
        for i in range(len(requests)):
            l,r = requests[i]
            
            prefix_sum[l] += 1
            prefix_sum[r + 1] -= 1
        
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
        
        res = 0
        prefix_sum.sort(reverse=True)
        nums.sort(reverse=True)
        
        for i in range(len(nums)):
            if prefix_sum[i] == 0:
                break
        
            res += (prefix_sum[i] * nums[i])
        
        return res % (10**9 + 7)

            