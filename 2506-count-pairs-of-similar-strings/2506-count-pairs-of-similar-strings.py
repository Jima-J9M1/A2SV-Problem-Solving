class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        #loop through word and count each words to compare the keys of different words
        length = len(words)
        count = 0
        
        for index in range(length - 1):
            
            _dict1 = Counter(words[index])
            
            for key in range(index + 1,length):
                
                _dict2 = Counter(words[key])
                
                if _dict1.keys() == _dict2.keys():
                    count += 1
                    
        return count
            
            
            
        