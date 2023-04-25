class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = [0] 
        self.mergeSort(nums, 0, len(nums) - 1, res)
        
        return res[0]
    def merge(self,left, right, res):
        right_ptr1 = len(right) - 1
        left_ptr1 = len(left) - 1
        
        
        while right_ptr1 >= 0 and left_ptr1 >= 0:
            if left[left_ptr1] > (2 * right[right_ptr1]):
                val = (len(right) - 1) - right_ptr1
                res[0] += (len(right) - val)
                left_ptr1 -= 1
            else:
                right_ptr1 -= 1
                
        
        
        
        
        ptr1 = 0
        ptr2 = 0
        merge_list = []
        
        while ptr1 < len(left) and ptr2 < len(right):
            if left[ptr1] <= right[ptr2]:
                merge_list.append(left[ptr1])
                ptr1 += 1
            else:
                merge_list.append(right[ptr2])

                ptr2 += 1
        
        if ptr1 < len(left):
            merge_list += left[ptr1:]
        
        if ptr2 < len(right):
            merge_list += right[ptr2:]
                
        return merge_list
    
    def mergeSort(self, nums, left, right, res):
        if left == right:
            return [nums[left]]
        mid = left + (right - left) // 2
        
        left_half = self.mergeSort(nums, left, mid, res)
        right_half = self.mergeSort(nums, mid + 1, right, res)
        
        
        return self.merge(left_half, right_half, res)
        