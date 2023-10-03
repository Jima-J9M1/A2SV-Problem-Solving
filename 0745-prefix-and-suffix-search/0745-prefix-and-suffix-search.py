class TrieNode:
    def __init__(self):
        self.kids = {}
        self.suffixs = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word, indx):
        cur = self.root

        for ch in word:
            if ch not in cur.kids:
                cur.kids[ch] = TrieNode()

            cur = cur.kids[ch]
            for i in range(len(word) - 1, -1, -1):
                suf = word[i:]
                cur.suffixs[suf] = indx


    def search(self, pref, suff):
        cur = self.root

        for ch in pref:
            if ch not in cur.kids:
                return -1

            cur = cur.kids[ch]
        
        return cur.suffixs[suff] if suff in cur.suffixs else -1


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for indx, word in enumerate(words):
            self.trie.insert(word, indx)




    def f(self, pref: str, suff: str) -> int:
        ans = self.trie.search(pref, suff)

        return ans
        
#         res = []
#         for indx, val in enumerate(self.pref_words):
#             if indx in ans:
#                 res.append((val, indx))
             
#         res.sort()
#         return res[0][1]
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)