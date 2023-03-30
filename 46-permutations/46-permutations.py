class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = 0
        result = [[]]
        self.backTracking(nums, visited, [], result)
        
        return result[0]
        
    def backTracking(self, nums, visited, path, result):
        if len(nums) == len(path):
            result[0].append(path[:])
            return
        
        for indx in range(len(nums)):
            if nums[indx] < 0:
                shift = 1 << (10 - (nums[indx]))
                
            else:
                shift = 1 << nums[indx]
            
            if visited & shift == 0:
                visited |= (shift)
                path.append(nums[indx])
                self.backTracking(nums, visited, path, result)
                val = path.pop()
                
                if val < 0:
                    visited ^=  1 << (10 - (val))
                else:
                    visited ^= 1 << val
            
            
            
        """
        visited = set()
        result = [[]]
        self.backTracking(nums, visited, [], result)
        
        return result[0]
    
    def backTracking(self, nums, visited, path, result):
        if len(path) == len(nums):
            result[0].append(path[:])
            return
        
        for indx in range(len(nums)):
            
            if nums[indx] not in visited:
                visited.add(nums[indx])
                path.append(nums[indx])
                self.backTracking(nums, visited,  path, result)
                val = path.pop()
                visited.remove(val)
                
                """
                
            
        