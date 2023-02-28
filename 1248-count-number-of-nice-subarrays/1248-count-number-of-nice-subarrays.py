class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for idx in range(len(nums)):
            if nums[idx] % 2 == 0:
                nums[idx] = 0
            else:
                nums[idx] = 1
        
        cur_sum = 0
        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        
        for idx in range(len(nums)):
            cur_sum += nums[idx]
            
            if (cur_sum - k) in dic:
                count += dic[cur_sum - k]
                
            dic[cur_sum] += 1
            
        
        return count
        