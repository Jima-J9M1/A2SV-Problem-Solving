class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
            
        left = m - 1
        right = n -1
        flag = (m + n) - 1
        
        while (left >= 0 and right >= 0):
            
            if nums1[left] <= nums2[right]:
                nums1[flag] = nums2[right]
                right -= 1
                flag -= 1
            else:
                nums1[flag] = nums1[left]
                left -= 1
                flag -= 1
       
        while right >= 0:
            nums1[flag] = nums2[right]
            right -= 1
            flag -= 1
        