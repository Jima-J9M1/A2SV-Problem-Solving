class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = 0
        result = [[]]
        self.backTracking(nums, visited, [], result)
        
        return result[0]
        
        """
        @param: nums -> input list
        @param: visited -> it mark visited number with bit manipulation
        @param: path -> store not visited number in the list
        @param: result -> store permutation of the nums in the result
        """
    def backTracking(self, nums, visited, path, result):
        if len(nums) == len(path):
            result[0].append(path[:])
            return
        
        for indx in range(len(nums)):
            # number is negative, shift 1bit to the left 10  + current number times and store the element in that pos
            if nums[indx] < 0:
                shift = 1 << (10 - (nums[indx]))
            
            # number is postive, shift 1bit to the left  current number times and store the element in that pos
            else:
                shift = 1 << nums[indx]
            
            #check if the visited number and operator shift value gives 0 then the position is not visited 
            if visited & shift == 0:
            
                #assign the postion of the number to be visited
                visited |= (shift)
                path.append(nums[indx])
                self.backTracking(nums, visited, path, result)
                val = path.pop()
                
                #if negative, to remove shift 1bit to the left 10 times + popped value times 
                #And do the XOR operation
                
                if val < 0:
                    visited ^=  1 << (10 - (val))
               #postive, shift  1bit to the left times the poped value and do XOR operation     
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
                
            
        