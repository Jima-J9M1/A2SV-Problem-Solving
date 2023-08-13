class Solution:
    def find(self, size, rep, x):
        root = x
        while root != rep[root]:
            root = rep[root]
            
        while x != root:
            parent = rep[root]
            rep[root] = root
            x = parent
            
        return root
    
    def union(self, size, rep, x, y):
        rep_x = self.find(size, rep, x)
        rep_y = self.find(size, rep, y)
        
        if rep_x == rep_y:
            return
        
        if size[rep_x] > size[rep_y]:
            rep[rep_y] = rep_x
            size[rep_x] += size[rep_y]
        else:
            rep[rep_x] = rep_y
            size[rep_y] += size[rep_x]
            

    def removeStones(self, stones: List[List[int]]) -> int:
        #goal: largest number of stones removed
        #[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] st0(1,2) -> st1(2,3,4) -> st2(1,3,4) -> st3(1,2,4,5) -> st4(1,2,3,5) -> st5(3,4)
        # st0(1,2,3,4,5)
        # edge case: when there is no conected stones 
        # algorthim to find the largest number of stones removed
        # create a helper function find and union
        # represet connective stone with the same representative
        # and calculate the size of the stone under one representative
        # calculate the size of each distnict representative with out including the representative
        # return the calculate size
        
        representative = {i:i for i in range(len(stones))}
        size = [1] * len(stones)
        
        for indx, stone in enumerate(stones):
            for j in range(indx, len(stones)):
                if stone[0] == stones[j][0] or stone[1] == stones[j][1]:
                    self.union(size, representative, indx, j)
                  
        ans = 0
        for rep in representative:
            if rep == representative[rep]:
                ans += size[rep] - 1
        
        return ans
                    
        
        
        