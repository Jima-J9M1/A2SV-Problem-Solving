class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        val = sorted(nums1)
        
        if len(val) % 2 == 1:
            return val[len(val)//2]/ 1.0
        
        else:
            return (val[len(val)//2] + val[(len(val)//2) - 1]) / 2
        
        
        