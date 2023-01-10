class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [[-1,-1],[0,-1],[-1,0],[-1,1],[1,-1],[0,1],[1,1],[1,0]]
        ans = []
        
        queen_check = set(map(tuple,queens))

        
        for pos in directions:
            row,col = king
            
            while 0 <= row < 8 and 0 <= col < 8:
                
                row  +=  pos[0]
                col += pos[1]
                
                if (row,col) in queen_check:
                    ans.append([row,col])
                    break
        return ans