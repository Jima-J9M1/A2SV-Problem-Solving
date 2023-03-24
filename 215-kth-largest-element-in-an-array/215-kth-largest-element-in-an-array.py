class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def merge(nums1, nums2):
            ptr1 = 0
            ptr2 = 0
            ans = []
            # print(nums1, nums2)
            while ptr1 < len(nums1) and ptr2 < len(nums2):
                
                if nums1[ptr1] < nums2[ptr2]:
                    ans.append(nums1[ptr1])
                    ptr1 += 1
                    
                else:
                    ans.append(nums2[ptr2])
                    ptr2 += 1
                    
            
            if ptr1 < len(nums1):
                ans += nums1[ptr1:]
                
            if ptr2 < len(nums2):
                ans += nums2[ptr2:]
                
            return ans
        
        def mergeSort(left,right, nums):
            if left == right:
                return [nums[left]]
            
            mid = left + (right - left ) // 2 
            
            left = mergeSort(left, mid, nums)
            right = mergeSort(mid + 1 , right, nums)
            
            return merge(left, right)
        
        ans = mergeSort(0, len(nums)- 1, nums)
        return ans[-k]