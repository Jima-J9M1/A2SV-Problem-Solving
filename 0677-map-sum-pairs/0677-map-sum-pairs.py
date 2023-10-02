class TrieNode:
    def __init__(self):
        self.kids = [[None, -1]]* 26
        self.isEnd = False
        self.prevVal = -1
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        
        for ch in key:
            indx = ord(ch) - ord('a')
            if cur.kids[indx][0] == None:
                cur.kids[indx] = [TrieNode(), val]
            else:
                cur.kids[indx][1] += val
                
            
            cur = cur.kids[indx][0]
            
        
        if cur.isEnd:
            prev = cur.prevVal
            cur = self.root
            
            for ch in key:
                indx = ord(ch) - ord('a')

                cur.kids[indx][1] -= prev

                cur = cur.kids[indx][0]
                
            cur.prevVal = val
            
        else:
            cur.isEnd = True
            cur.prevVal = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        
        val = 0
        for ch in prefix:
            indx = ord(ch) - ord('a')
            
            if cur.kids[indx][0] != None:
                val = cur.kids[indx][1]
                cur = cur.kids[indx][0]
                
            else:
                return 0
            
        return val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)