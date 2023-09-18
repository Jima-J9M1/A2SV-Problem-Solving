class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        paths =[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        rep = {}
        
        
        def find(node):
            parent = node
            
            while parent != rep[parent][0]:
                parent = rep[parent][0]
                
            while node != parent:
                root = rep[node][0]
                rep[node][0] = parent
                node = root
                
            return parent
        
        def union(node1, node2):
            rep_n1 = find(node1)
            rep_n2 = find(node2)
            
            if rep_n1 == rep_n2:
                return 
            
            rep[rep_n2][0] = rep_n1 
            _, left_col, right_col = rep[rep_n2]
            rep[rep_n1][1] = rep[rep_n1][1] or left_col
            rep[rep_n1][2] = rep[rep_n1][2] or right_col
            
            
        for prev_val, (nrow, ncol) in enumerate(cells):
            
            left_col = ncol == 1
            right_col = ncol == col
            
            rep[(nrow, ncol)] = [(nrow, ncol), left_col, right_col]
            
            for nr, nc in paths:
                path = (nr + nrow, ncol + nc)
                
                if path not in rep:
                    continue
                    
                union((nrow, ncol), path)
                
            parent = find((nrow, ncol))
            
            _, left_col, right_col = rep[parent]
            
            if left_col and right_col:
                return prev_val
        
        return -1
            
            
            
            
            
            
            
            
            
            