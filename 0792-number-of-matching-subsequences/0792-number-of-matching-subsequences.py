class TrieNode:
    def __init__(self):
        self.kids = [None] * 26
        self.isEnd = False
        
    
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            indx = ord(ch) - ord('a')
            
            if cur.kids[indx] == None:
                cur.kids[indx] = TrieNode()
                
                
            cur = cur.kids[indx]
            
        cur.isEnd = True
        
    def search(self, word, word2):
        cur = self.root
        pos = 0
        pos1 = 0
        
        while pos < len(word) and pos1 < len(word2):
            indx = ord(word[pos]) - ord('a')
            indx2 = ord(word2[pos1]) - ord('a')
            
            if cur.kids[indx] != None:
                pos += 1
                pos1 += 1
                cur = cur.kids[indx]
                
            else:

                cur = cur.kids[indx2]
                pos1 += 1
                
                
                
        if pos >= len(word):
            return True
        
        return False

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        TestTrie = Trie()
        
        TestTrie.insert(s)
        
        ans = 0
        Dic_word = dict()
        
        for word in words:
            
            if word not in Dic_word:
                check = TestTrie.search(word, s)
                Dic_word[word] = check
            else:
                check = Dic_word[word]
                
                
            if check:
                ans += 1
                
               
        return ans
            