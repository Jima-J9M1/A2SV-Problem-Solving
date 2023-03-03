class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def binarySearch(nums,low,high,target,turn):
            best = -1
            
            while low <= high:
                
                mid = low + (high - low) // 2
                
                if nums[mid] > target:
                    high = mid - 1
                    
                elif nums[mid] < target:
                    low = mid + 1
                    
                else:
                    best = mid
                    
                    if turn:
                        high = mid - 1
                    else:
                        low = mid + 1
            
            return best
        
        first_pos = binarySearch(nums,0,len(nums) - 1,target,True)
        last_pos = binarySearch(nums,0,len(nums) - 1,target,False)
        
        return [first_pos,last_pos]