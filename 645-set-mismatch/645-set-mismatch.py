class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = [0] * 2
        
        
        for idx in range(1, len(nums) + 1):
            if count[idx]:
                if count[idx] > 1:
                    ans[0] = idx
            else:
                ans[1] = idx
        
        return ans
        
                    