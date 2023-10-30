class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        
        
        for i in range(len(nums)):
            val = target  - nums[i]
            if val in hashmap:
                val = target - nums[i]
                return [hashmap[val], i]
            
            hashmap[nums[i]] = i
            
            
        return -1
            
            