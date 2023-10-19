class TrieNode:
    def __init__(self):
        self.kids = {}
        self.is_end = False
        
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            
            if ch not in cur.kids:
                cur.kids[ch] = TrieNode()
                
            cur = cur.kids[ch]
            
        cur.is_end = True
            
    def searchWord(self, word):
        cur = self.root
        ans = ""
        res = set()
        for ch in word:
            if cur.is_end == True:
                res.add(ans)
                return res
            
            ans  +=  ("/" + ch)
                
            cur = cur.kids[ch]
            
        res.add(ans)
        return res
        
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        for ele in folder:
            words = ele.split('/')
            words.remove('')
            self.insert(words)
            
        res = set()
        for ele in folder:
            words = ele.split('/')
            words.remove('')
            ans = self.searchWord(words)
            res |= ans
            
        
        return res
                
        