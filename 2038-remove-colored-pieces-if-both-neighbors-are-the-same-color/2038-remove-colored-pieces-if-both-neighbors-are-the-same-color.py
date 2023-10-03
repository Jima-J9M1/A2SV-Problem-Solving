class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        
        alpha = defaultdict(int)
        flag = False
        
        
        right  = 0
        let = colors[0]
        left = 0
        while right < len(colors):
              
            if let != colors[right]:
                left = right 
                let = colors[right]
                
            right += 1
            if (right - left) == 3:
                alpha[let] += 1
                left += 1
                
        # print(alpha)
        if alpha["A"] > alpha["B"]:
            flag = True
        
        
        return flag
                
               
                