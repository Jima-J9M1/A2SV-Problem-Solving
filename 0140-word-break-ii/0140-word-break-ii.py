class Trie:
    def __init__(self):
        self.kids = {}
        self.is_end = False
        
        
        
class Solution:
    
    def __init__(self):
        self.root = Trie()
        
        
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            if ch not in cur.kids:
                cur.kids[ch] = Trie()
                
            cur = cur.kids[ch]
            
        cur.is_end = True
        
        
    def search(self, word):
        cur = self.root
        
        for ch in word:
            if ch not in cur.kids:
                return False
            
            cur = cur.kids[ch]
            
        return cur.is_end
    
    
    def solve(self, s, st, pos, ans):
        if pos == len(s):
            ans.append(st)
            
        st += " "
        
        for i in range(pos, len(s)):
            val = self.search(s[pos:i + 1])
            
            
            if val:
                self.solve(s, st + s[pos:i + 1], i + 1, ans)
            
                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        for word in wordDict:
            self.insert(word)
            
        ans = []
        for i in range(len(s)):
            if self.search(s[:i + 1]):
                self.solve(s, s[:i +  1], i + 1,ans)
                
                
        return ans
        
#         def helper(s, memo, wordDict):
#             if s in memo:
#                 return memo[s]
            
#             if not s:
#                 return []
            
#             res = []
            
#             for word in wordDict:
#                 if not s.startswith(word):
#                     continue
                    
#                 if len(s) == len(word):
#                     res.append(word)
#                     continue
                    
                    
#                 result = helper(s[len(word):], memo, wordDict)
                
#                 for item in result:
#                     item = word + ' ' + item
#                     res.append(item)
                    
            
#             memo[s] = res
            
#             return res
        
#         memo = {}
        
#         return helper(s, memo, wordDict)
                