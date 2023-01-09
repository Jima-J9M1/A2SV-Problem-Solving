class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        rule = [[-1,-1],[0,-1],[-1,0],[-1,1],[1,-1],[0,1],[1,1],[1,0]]
        ans = []
        
        for ele in rule:
            new_king = king
            
            while (new_king[0] >= 0 and new_king[1] >= 0 ) and (new_king[0] <= 8 and new_king[1] <= 8 ) :
                val_1 = new_king[0] + ele[0]
                val_2 = new_king[1] + ele[1]
                new_king = [val_1,val_2]
                if new_king in queens:
                    ans.append(new_king)
                    break
        return ans