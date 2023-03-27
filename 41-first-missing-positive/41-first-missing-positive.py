class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        
        for idx in range(len(nums)):
            if nums[idx] < 0 or nums[idx] >= len(nums):
                nums[idx] = 0
        
        for idx in range(len(nums)):
            nums[nums[idx] % n] += n
            
        for idx in range(1,len(nums)):
            if nums[idx] // n == 0:
                return idx
        
        
        
        return n
        
        
        
        """
        count = Counter(nums)
        ans = 0
        
        if len(nums) == 1:
            if nums[-1] == 1:
                ans = 2
            else:
                ans = 1
        
        for idx in range(1, len(nums) + 1):
            if not count[idx]:
                ans = idx
                break
                
        if ans == 0:
            ans = idx + 1
            
        return ans
        """