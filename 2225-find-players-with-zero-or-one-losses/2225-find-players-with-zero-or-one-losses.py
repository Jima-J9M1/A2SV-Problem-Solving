class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        _dict = defaultdict(int)
        length = len(matches)
        
        for elem in matches:
            win,los = elem
            
            if win not in _dict:
                _dict[win] = 1
                
            else:
                if _dict[win] < 0: 
                    pass
            
            
            if los not in _dict:
                _dict[los] = -1
            else:
                if _dict[los] == 1:
                    _dict[los] = -1
                else:
                    _dict[los] += -1
        
        new_val = []
        new_val2 = []
        
        for key in _dict:
            
            if _dict[key] == 1:
                new_val.append(key)
                
            elif _dict[key] == -1:
                new_val2.append(key)
                
        print(new_val,new_val2)
        return [sorted(new_val), sorted(new_val2)]
                
            
                
        