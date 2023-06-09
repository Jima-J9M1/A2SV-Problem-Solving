class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_val = '-1'
        
        for ele in letters:
            if ele > target and (ele < min_val or min_val == '-1'):
                min_val = ele
                
                
                
        return min_val if min_val  != '-1' else letters[0]