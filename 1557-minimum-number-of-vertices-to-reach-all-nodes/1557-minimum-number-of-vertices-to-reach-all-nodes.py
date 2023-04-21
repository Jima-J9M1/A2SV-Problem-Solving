class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        for edge in edges:
            v1, v2 = edge
            graph[v1].append(v2)
            visited.add(v2)
        
        res = []
        for indx in range(n):
            if indx not in visited:
                res.append(indx)
                
        return res