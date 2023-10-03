class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_num = Counter(nums)
        
        num_goods = 0
        for key in freq_num:
            if freq_num[key] > 1:
                n = freq_num[key]
                num_goods += (n - 1)*(n)// 2
                
                
        return num_goods
                