class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_val = max(nums)
        min_val = 0
        
        if min(nums) < 0:
            min_val = abs(min(nums))
            count_num = [0] * (max_val + min_val + 1)
        else:
            count_num = [0] * (max_val + 1)
        
        #count the value of the ele in nums and store it into with count_num with their index         
        for index in range(len(nums)):
            count_num[nums[index] + abs(min_val)] += 1
        
        val = 0
        count = 0
        
        #count ele in count_num from reversed if the elem is greater than zero and compare to k          
        
        for index in range(len(count_num) - 1,-1,-1):
            if count_num[index] > 0:
                count += count_num[index]
                if count >= k:
                    val = index - min_val
                    break
        
        return val