class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) < m * n or len(original) > m * n:
            return []
        
        matrix = []
        length = len(original)
        new_val = []
        
        
        #create new 2D array from 1D array
        for index in range(length):
            new_val.append(original[index])
            if len(new_val) == n:
                matrix.append(new_val)
                new_val = []
        return matrix
        