class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = set()
        set_nums2 = set(nums2)
        set_nums1  = set(nums1)
        if len(nums1) > len(nums2):
            for index in range(len(nums1)):
                if nums1[index] in set_nums2:
                    res.add(nums1[index])
        else:
            for index in range(len(nums1)):
                if nums1[index] in set_nums2:
                    res.add(nums1[index])
                
        return list(res)
            
            