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
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for ch in prefix:
            index = ord(ch) - ord('a')
            
            
            if node.kids[index] == None:
                return False
            
            node = node.kids[index]
            
            
        return True
    
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        TrieNode = Trie()
        for word in strs:
            TrieNode.insert(word)
            
            
        prefix = ""
        
        node = TrieNode.root
        st = "val"
        res = ""
        
        
        while st != "":
            count = 0
            check = True
            s = "*"
            
            for indx,val in enumerate(node.kids):
                if val != None:
                    count += 1
                    next = indx
                    s = chr(97 + next)
            

            for word in strs:
                if (s and s not in word) or (len(res) + 1 > len(word)) :
                    check = False
                    
            if not check:
                break
                
            if count == 1:
                node = node.kids[next]
                res += s
            else:
                st = ""
                
                    
                    
        for word in strs:
            if word == "" and res:
                return ""
                
        return res
        
        
        
        
        