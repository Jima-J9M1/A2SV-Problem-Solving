class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        max_val = 0
        bit_map = self.bit_map(words)
        
        for index in range(len(words)):

            for i in range(index + 1, len(words)):

        
                if bit_map[index] & bit_map[i] == 0:
                    max_val = max(len(words[index]) * len(words[i]), max_val)
                    
                    
        return max_val
                
        
    def bit_map(self,words):
        res = []
        
        for word in words:
            bit_rep = 0
            for char in word:
                shift_bit = 1 << (ord(char) - ord('a'))
                bit_rep  |= shift_bit
                
            res.append(bit_rep)
        

        return res
    