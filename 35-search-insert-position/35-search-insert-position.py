class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        
        if target < nums[l]:
            return l
        if target > nums[r]:
            return len(nums)
        
        while r >= l:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif mid > 0 and nums[mid-1] < target < nums[mid]:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return len(nums)
                    
        