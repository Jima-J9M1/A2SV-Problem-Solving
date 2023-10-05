class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        freq_formula = len(nums) // 3
        
        ans = []
        for key in freq:
            if freq[key] > freq_formula:
                ans.append(key)
                
        return ans
            