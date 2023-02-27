class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        right = 0
        prefix_sum = [0] * len(nums)
        count = 0
        
        
        for i in range(len(nums)):
            prefix_sum[i] = prefix_sum[i -1] + nums[i]
            
            
            
        while right < len(prefix_sum):
            
            if (prefix_sum[right] % k) in dic:
                count += dic[prefix_sum[right] % k]
            
            dic[prefix_sum[right] % k] += 1
            right += 1
        
        
        return count