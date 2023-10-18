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
    
        
    def union(self, rep, word_1, word_2):
        rep_word1 = self.find(rep, word_1)
        rep_word2 = self.find(rep, word_2)
        
        if rep_word1 == rep_word2:
            return 
        
        if rep_word1 == 0:
            rep[rep_word2] = 0
            return
            
        if rep_word2 == 0:
            rep[rep_word1] = 0
            return 
        
        rep[rep_word1] = rep_word2
        
            
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        
        
        same_time = defaultdict(list)
        
        rep = {i:i for i in range(n)}
        
        rep[firstPerson] = 0
        
        
        for p1, p2, time in meetings:
            same_time[time].append([p1,p2])
            
        
        for key in sorted(same_time):
            for p1, p2 in same_time[key]:
                self.union(rep, p1, p2)
                
            for p1, p2 in same_time[key]:
                y1 = self.find(rep, p1)
                x1 = self.find(rep, p2)
                
                if y1 != 0:
                    rep[p1] = p1
                    
                if x1 != 0:
                    rep[p2] = p2
                
            
        
        
        
        val = rep[0]
        
        ans = []
        for key in rep:
            if rep[key] == val:
                ans.append(key)
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        