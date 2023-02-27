class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        
        cur = 0
        right = 0
        count = 0
        
        while right < len(nums):
            cur += nums[right]
            
            if cur - k in dic:
                count += dic[cur - k]
                
            dic[cur] += 1
            right += 1
            
        return count
        
        