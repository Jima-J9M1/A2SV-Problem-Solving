class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result.append(matrix[row][col])
        
        heapify(result)
        
        for i in range(k - 1):
            heappop(result)
        ans = heappop(result)
        return ans
                
                