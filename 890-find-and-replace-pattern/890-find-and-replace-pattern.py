class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        
        res = []
        
        
        for word in words:
            
            count_pattern = defaultdict(int)
            count_word = defaultdict(int)
            flag = True
            
            for i in range(len(word)):
                count_pattern[pattern[i]] += 1
                count_word[word[i]] += 1
                
                val = list(count_pattern.values())
                val2 = list(count_word.values())
                
                if val != val2:
                    flag = False
                    
            if flag:   
                res.append(word)
        
        return res