class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return 
        
        _dict = defaultdict(list)
        
        i = 97
        j = 2
        while i < 123:
            _dict[j].append(chr(i))
            
            if len(_dict[j]) == 3 and j != 7 and j != 9:
                j += 1
                
            elif len(_dict[j]) == 4:
                j += 1
            
            i += 1
        
        
        res = []
        
        
        for j in _dict[int(digits[0])]:
            
            if len(digits) == 1:
                st = j
                res.append(j)
                continue
                
            for k in _dict[int(digits[1])]:
                
                if len(digits) == 2:
                    st = j + k
                    res.append(st)
                    continue
                    
                for l in _dict[int(digits[2])]:
                    
                    if len(digits) == 3:
                        st = j + k + l
                        res.append(st)
                        continue
                        
                    for m in _dict[int(digits[3])]:
                        
                        st = j + k + l + m
                        res.append(st)
        
        return res
        
