class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction) 
        dp = [0] * (n + 1)
        
        max_val = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                dp[j] = (satisfaction[j] * (j - i + 1) + dp[j + 1])
            
            max_val = max(dp[i], max_val)
                
                
        return max_val
                