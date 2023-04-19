class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        res = [0]
        merge_list = []
        
        for indx in range(len(nums1)):
            merge_list.append(nums1[indx] - nums2[indx])
        
        
        self.mergeSort(merge_list, 0, len(merge_list) - 1, res,diff)
        
        return res[0]
        
    def merge(self,left, right, res,diff):
        right_ptr1 = 0
        left_ptr1 = 0
        
        while left_ptr1 < len(left) and right_ptr1 < len(right):
            if left[left_ptr1] <= (diff + right[right_ptr1]):
                res[0] += (len(right) - right_ptr1)
                left_ptr1 += 1
            else:
                right_ptr1 += 1
                
                
        
        ptr1 = 0
        ptr2 = 0
        merge_list = []
        
        while ptr1 < len(left) and ptr2 < len(right):
            if left[ptr1] <= right[ptr2]:
                merge_list.append(left[ptr1])
                ptr1 += 1
            else:
                merge_list.append(right[ptr2])
                # if left[ptr1] > (2 * right[ptr2]):
                #     print("here", left[ptr1], right[ptr2])
                ptr2 += 1
        
        if ptr1 < len(left):
            merge_list += left[ptr1:]
        
        if ptr2 < len(right):
            merge_list += right[ptr2:]
                
        return merge_list
    
    def mergeSort(self, nums, left, right, res,diff):
        if left == right:
            return [nums[left]]
        mid = left + (right - left) // 2
        
        left_half = self.mergeSort(nums, left, mid, res,diff)
        right_half = self.mergeSort(nums, mid + 1, right, res,diff)
        
        return self.merge(left_half, right_half, res,diff)