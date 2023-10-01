class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
    
        arr = []
        for i in range(n):
            arr.append((ages[i], scores[i]))
            
        arr.sort(key=lambda x:(x[0], x[1]), reverse=True)
        
        dp = [0]*n
        dp[-1] = arr[-1][1]
        print(arr)
        for i in range(n - 2, -1, -1):
            max_val = 0
            for j in range(i + 1, n):
                if (arr[i][1] >= arr[j][1]) or arr[i][0] == arr[j][0]:
                    max_val = max(max_val, dp[j])
                    
            dp[i] = arr[i][1] + max_val
            
        
        return max(dp)
        
