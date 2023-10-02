class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEnd = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        cur = self.root
        
        if len(word) == 1:
            cur.kids[word[-1]] = TrieNode()
            return True
        
        
        count = 0
        
        for ch in word:
            if ch not in cur.kids:
                count += 1
                
                if count > 1:
                    return False
                
            else:
                cur = cur.kids[ch]
                
        cur.kids[word[-1]] = TrieNode()
        cur.isEnd = True
        
        
        return True
    
    
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key=lambda x:len(x))
        TrieDSA = Trie()
        ans = []
        
        for word in words:
            if TrieDSA.insert(word):
                ans.append(word)
            
        if not ans:
            return ""
        ans.sort(key=len)
        
        max_val = len(ans[-1])
        
        res = sorted(filter(lambda x:len(x) == max_val, ans))
        
        return res[0]
                
                
        
        
        
        
        
        
        
        
        
        
        
        