class TrieNode:
    def __init__(self):
        self.kids = [None] * (26)
        self.isEOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            index = ord(ch) - ord('a')
            
            if node.kids[index] == None:
                node.kids[index] = TrieNode()
                
            node = node.kids[index]
            
        node.isEOW = True
        

    def search(self, word: str) -> bool:
        node = self.root
        
        for ch in word:
            index = ord(ch) - ord('a')
            
            
            if node.kids[index] == None:
                return False
            
            
            node = node.kids[index]
            
        if node.isEOW:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for ch in prefix:
            index = ord(ch) - ord('a')
            
            
            if node.kids[index] == None:
                return False
            
            node = node.kids[index]
            
            
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)