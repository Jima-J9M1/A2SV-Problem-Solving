class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
        n = len(text1)
        m = len(text2)
        
        
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i][j + 1], grid[i + 1][j])
                    
        return grid[0][0]