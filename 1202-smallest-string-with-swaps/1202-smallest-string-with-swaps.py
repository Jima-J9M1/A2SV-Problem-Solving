class Solution:
    def find(self,rep, size, x):
        parent = x
        
        while parent != rep[parent]:
            parent = rep[parent]
            
        while x != parent:
            root = rep[x]
            rep[x] = parent
            x = root
            
        return parent
    
    def union(self, rep, size, x, y):
        rep_x = self.find(rep, size, x)
        rep_y = self.find(rep, size, y)
        
        
        if rep_x == rep_y:
            return 
        
        
        if size[rep_x] > size[rep_y]:
            rep[rep_y] = rep_x
        elif size[rep_y] > size[rep_x]:
            rep[rep_x] = rep_y
        else:
            rep[rep_y] = rep_x
            size[rep_x] += 1
            
        
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #goal: to return lexicographicl smallest string 
        #edge case string has 1 ele
        #edge case no pairs
        
        
        representative = {i : i for i in range(len(s))}
        size = [1] *len(s)
        
        for s1,s2 in pairs:
            self.union(representative, size, s1, s2)
            
        rep_string = defaultdict(list) 
        rep_indx = defaultdict(list)
        for indx in range(len(s)):
            rep_s = self.find(representative, size, indx)
            representative[indx] = rep_s
            rep_string[rep_s].append(s[indx])
            rep_indx[rep_s].append(indx)
        
        ans = ['']*len(s)
        
        for key in rep_string:
            sorted_val = sorted(rep_string[key])
            for indx, ele in enumerate(sorted_val):
                indx = rep_indx[key][indx]
                ans[indx] = ele
                
        return "".join(ans)
    