class Solution:
    def find(self, rep, word):
        root = word
        
        while root != rep[root]:
            root = rep[root]
            
        while word != root:
            parent = rep[word]
            rep[word] = root
            word = parent
            
        
        return root
    
        
    def union(self, rep, size, word_1, word_2):
        rep_word1 = self.find(rep, word_1)
        rep_word2 = self.find(rep, word_2)
        
        if rep_word1 == rep_word2:
            return 
        
        if size[rep_word1] > size[rep_word2]:
            rep[rep_word2] = rep_word1
            
        elif size[rep_word2] > size[rep_word1]:
            rep[rep_word1] = rep_word2
            
        else:
            rep[rep_word2] = rep_word1
            size[rep_word1] += 1
            
            
        
        
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        ch_len = len(strs[0])
        
        rep = {i:i for i in range(n)}
        
        size = [0]*n
        
        
        
        for indx in range(n):
            for j in range(indx + 1, n):
                ptr = 0
                
                count = 0
                while ptr < ch_len:
                    if strs[indx][ptr] != strs[j][ptr]:
                        count += 1
                        
                    ptr += 1
                    
                
                if count <= 2:
                    self.union(rep, size, indx, j)
                    
            
        ans = set()
        for i in range(n):
            rep_ele = self.find(rep, i)
            ans.add(rep_ele)
            
        
        return len(ans)
                
        