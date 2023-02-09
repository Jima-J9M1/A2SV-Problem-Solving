class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        hashMap = defaultdict(set)
        res = 0
        for word in ideas:
            hashMap[word[0]].add(word[1:])
        
        
        for char1 in hashMap:
            
            for char2 in hashMap:
                if char1 == char2:
                    continue
                    
                intersect = 0
                
                for word in hashMap[char1]:
                    if word in hashMap[char2]:
                        intersect += 1
                        
                
                distinict = len(hashMap[char1]) - intersect
                distinict2 = len(hashMap[char2]) - intersect
                
                res += distinict * distinict2
        
        return res