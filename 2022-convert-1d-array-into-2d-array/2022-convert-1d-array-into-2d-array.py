class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) < m * n or len(original) > m * n:
            return []
        
        matrix = []
        length = len(original)
        new_val = []
        ptr = 0
        ptr2 = n
        #create new 2D array from 1D array
        for _ in range(m):
            matrix.append(original[ptr:ptr2])
            ptr += n
            ptr2 += n
            
        # for index in range(length):
        #     new_val.append(original[index])
        #     if len(new_val) == n:
        #         matrix.append(new_val)
        #         new_val = []
        return matrix
        