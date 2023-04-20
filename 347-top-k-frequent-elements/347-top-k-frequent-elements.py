class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        non_duplicate_list = list(set(nums))
        ans = self.quickSort(non_duplicate_list, count)
        
        return ans[:k]
        
    def quickSort(self,nums, count):
        if len(nums) <= 1:
            return nums
        
        pivot = nums[0]
        less_freq = []
        more_freq = []
        right = 1
        
        while right < len(nums):
            if count[nums[right]] > count[pivot]:
                more_freq.append(nums[right])
            else:
                less_freq.append(nums[right])
            
            right += 1
                
        return self.quickSort(more_freq,count) + [pivot] + self.quickSort(less_freq, count)
    
        