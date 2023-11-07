class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        count = 0
        
        nums.sort(reverse=True)
        
        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    left += 1
                    
                else:
                    right -= 1
                    
        return count
    
    
    
#         nums.sort()
        
#         count = 0
#         for i in range(len(nums)):
#             k = i + 2
            
#             if nums[i] != 0:
#                 for j in range(i + 1, len(nums)):

#                     start = k
#                     end = len(nums) - 1

#                     res = None


#                     while start <= end:
#                         mid = start + (end - start) // 2

#                         if nums[i] + nums[j] > nums[mid]:
#                             res = mid
#                             start = mid + 1
#                         else:
#                             end = mid - 1

#                     if res:
#                         count += res - j
#                         k = res
                        
                        
                        
#         return count