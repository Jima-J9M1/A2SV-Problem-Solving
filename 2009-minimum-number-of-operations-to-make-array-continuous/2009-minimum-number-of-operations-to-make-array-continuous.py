class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        max_gap, count = 0,0
        size = len(nums)
        prefix_sum = [0]*(size + 1)
        visited = set()
        
        for i,ele in enumerate(nums):
            if ele in visited:
                prefix_sum[i] = 1
            
            visited.add(ele)
            
        prefix_sum = list(accumulate(prefix_sum))
        
        for indx, val in enumerate(nums):
            range_ = val + size - 1
            indx_found = bisect_left(nums, range_)
            
            if indx_found == size:
                indx_found = size -1
                
            if nums[indx_found] > range_:
                indx_found -= 1
                
            if max_gap - count < (indx_found - indx) - (prefix_sum[indx_found] - prefix_sum[indx]):
                
                max_gap = indx_found - indx
                count = prefix_sum[indx_found] - prefix_sum[indx]
                
        return (size - (max_gap + 1)) + count
        
        