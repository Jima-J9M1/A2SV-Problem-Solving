class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        min_val = 0
        for num in nums:
            if num < min_val:
                min_val = num
        

        shift = 0
        for num in nums:
            if num < 0:
                sh = 1 << -(num) -1
            else:
                sh = 1 << (num + (-min_val))
                
            shift ^= sh
            

        for num in nums:
            if num < 0:
                sh = 1 << -(num) -1
            else:
                sh = 1 << (num + (-min_val))
            ans = shift & sh
            if ans > 0:
                return num