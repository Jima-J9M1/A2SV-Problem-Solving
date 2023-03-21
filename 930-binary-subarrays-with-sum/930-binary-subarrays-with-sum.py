class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix_sum[i]  = prefix_sum[i - 1] + nums[i]
            
        _dict = Counter(prefix_sum)
        
        
        keys = list(_dict.keys())
        left = 0
        right = 0
        ans = 0
        
        '''
        Find subarray that is equal with goal, the goal is greater than 0  
        used a formual for consecutive numbers n(n + 1) // 2 
        '''
        while right < len(keys) and goal != 0:
            
            if keys[right] > goal:
                if _dict[keys[right] - goal]:
                    
                    ans += (_dict[keys[right] - goal] * _dict[keys[right]])
                    
            elif keys[right] == goal:
                if _dict[keys[right] - goal]:
                    ans += (_dict[keys[right] - goal] * _dict[keys[right]])
                    
                ans += (_dict[keys[right]])
            
            right += 1
            
        left = 0
        right = 0
        
        '''
        Find subarray sum which satisfy the goal 0
        Used a formula of consecutive number which is n(n + 1)/ 2
        
        '''
        while right < len(keys) and goal == 0:
            
            
            if keys[right] > goal and _dict[keys[right]] > 1:
                ans += ((_dict[keys[right]] - 1) * _dict[keys[right]])// 2
                
            elif keys[right] == goal:
                ans += (_dict[keys[right]] * (_dict[keys[right]] + 1))  // 2
            
            right += 1
            
        return ans