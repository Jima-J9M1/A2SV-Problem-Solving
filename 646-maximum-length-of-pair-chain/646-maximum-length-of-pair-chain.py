class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        memo = {}
        
        def dp(indx):
            if indx == 0:
                return 1
            
            if indx in memo:
                return memo[indx]
            
            max_length = 1
            for i in range(indx):
                if pairs[indx][0] > pairs[i][1]:
                    max_length = max(max_length, 1 + dp(i))
                    
                    
            memo[indx] = max_length
            return memo[indx]
        
        pairs.sort()
        
        max_length = 1
        
        for i in range(len(pairs)):
            max_length = max(max_length, dp(i))
            
        return max_length
        
        