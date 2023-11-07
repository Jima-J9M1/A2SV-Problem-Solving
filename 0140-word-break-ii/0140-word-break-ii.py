class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        def helper(s, memo, wordDict):
            if s in memo:
                return memo[s]
            
            if not s:
                return []
            
            res = []
            
            for word in wordDict:
                if not s.startswith(word):
                    continue
                    
                if len(s) == len(word):
                    res.append(word)
                    continue
                    
                    
                result = helper(s[len(word):], memo, wordDict)
                
                for item in result:
                    item = word + ' ' + item
                    res.append(item)
                    
            
            memo[s] = res
            
            return res
        
        memo = {}
        
        return helper(s, memo, wordDict)
                