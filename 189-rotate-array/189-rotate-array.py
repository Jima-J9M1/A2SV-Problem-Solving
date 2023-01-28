class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_val = k % len(nums)
        arr_len = len(nums)
        
        if arr_len > 1 and 0 < k <= arr_len:
            length = len(nums[:-k])
            nums[:k], nums[k:] = nums[-k:], nums[:length]
            
        elif arr_len > 1 and  k > arr_len:
            length = len(nums[:-new_val]) 
            nums[:new_val], nums[new_val:] = nums[-new_val:], nums[:length]