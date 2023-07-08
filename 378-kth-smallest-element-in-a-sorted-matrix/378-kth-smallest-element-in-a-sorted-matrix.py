class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result.append(matrix[row][col])
        result.sort()
        return result[k - 1]
                
                