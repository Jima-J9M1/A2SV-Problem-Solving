class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def binarySearch(nums,low,high,target):
            
            while low <= high:
                mid = (low + (high - low)//2)


                if nums[mid] < target:
                    low = mid + 1

                elif nums[mid] > target:
                    high = mid - 1

                else:

                    return mid
                
            return -1
        
        val = binarySearch(nums,0,len(nums) - 1,target)
        
        return val
        
        
                