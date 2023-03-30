class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
                
            # if len(path) == 0:
            #     visited = set()
        