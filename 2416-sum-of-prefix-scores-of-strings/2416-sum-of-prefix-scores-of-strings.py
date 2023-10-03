class TrieNode:
    def __init__(self):
        self.kids = {}
        self.count = 0
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            if ch not in cur.kids:
                cur.kids[ch] = TrieNode()
            
                
            cur = cur.kids[ch]
            cur.count += 1
            
    def search(self, word):
        cur = self.root
        ans = 0
        
        
        for ch in word:
           
            ans += cur.kids[ch].count
            cur = cur.kids[ch]
            
                
                
        return ans
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        result = []
        for word in words:

            res = trie.search(word)
            result.append(res)
            
        return result
        
        
        
        
        
        
        
        