class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.backTracking(nums, 0, [], result)
        
        return result[0]
           
    def backTracking(self, num,idx, path, result):
        if len(num) <= idx:
            return 
            
        for i in range(idx, len(num)):
            
            if len(path) == 0 or (path and path[-1] <= num[i]):
                path.append(num[i])
                if len(path) > 1 and path not in result[0]:
                    result[0].append(path[:])
                self.backTracking(num, i + 1, path, result)
                path.pop()
                
            