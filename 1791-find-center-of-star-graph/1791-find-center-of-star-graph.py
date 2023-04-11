class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        _dict = defaultdict(int)
        
        for row in range(len(edges)):
            for col in range(len(edges[0])):
                _dict[edges[row][col]] += 1
        
        for ele in _dict:
            if _dict[ele] == len(_dict) - 1:
                return ele
            
            