class NumArray:

    def __init__(self, nums: List[int]):
        self.pref_sum = [0]
        
        for  idx in range(len(nums)):
            val = self.pref_sum[idx] + nums[idx]
            self.pref_sum.append(val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right + 1] - self.pref_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)