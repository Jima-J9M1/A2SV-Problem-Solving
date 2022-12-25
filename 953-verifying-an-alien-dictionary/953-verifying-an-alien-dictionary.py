class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        left = 0
        right = 1
        length = len(words)
        
        
        if len(words) == 1:
            return True
        
        
        while right < length:
            min_size = min(len(words[left]),len(words[right]))
            index = 0
            while index < min_size:
                val_1 = order.index(words[left][index])
                val_2 = order.index(words[right][index])
                if val_1 > val_2:
                    return False
                elif val_1 < val_2:
                    if right == length - 1:
                        return True
                    else:
                        pass
                else:
                    pass
                index += 1
            right += 1
            right += 1
        
        if len(words[-2]) > len(words[-1]):
            return False
        
        return True
                
                