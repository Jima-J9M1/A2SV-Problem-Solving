class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i][j + 1], grid[i + 1][j])
                    
        return grid[0][0]