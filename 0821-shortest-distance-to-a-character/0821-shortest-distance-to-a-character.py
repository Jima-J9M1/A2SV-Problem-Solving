class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length = len(s)
        
        
        def shortedDistance(s, c):
            distance = [float("inf")] * length
            stack = []
             
            ptr = 0
            
            while ptr < length:
                
                if s[ptr] != c:
                    stack.append(ptr)
                    ptr += 1
                    continue
                    
                while stack and s[ptr] == c:
                    indx = stack.pop()
                    distance[indx] = ptr - indx
                    
                distance[ptr] = 0
                
                ptr += 1
                
            
            return distance
                    
                  
        reverse = s[::-1]
        right = shortedDistance(s, c)  
        left = shortedDistance(reverse, c)
        reverse_left = left[::-1]
        
        ans = []
        for i in range(length):
            ans.append(min(right[i], reverse_left[i]))
            
        return ans
            
            
            
            
            
        