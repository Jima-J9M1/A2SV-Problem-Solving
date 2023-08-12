class Solution:
    def find(self, rep, node):
        parent = node
        
        while parent != rep[parent]:
            parent = rep[parent]
            
        while node != parent:
            root = rep[node]
            rep[node] = parent
            node = root
        
        return parent
#         if node == rep[node]:
#             return node

#         ans = self.find(rep, rep[node])
#         rep[node] = ans
        
        
#         return ans
    
    def union(self, rep, node1, node2,size):
        parent_1 = self.find(rep, node1)
        parent_2 = self.find(rep, node2)
        
        if parent_1 == parent_2:
            return True
        
        else:
            if size[parent_1] > size[parent_2]:
                rep[parent_2] = parent_1
            elif size[parent_2] > size[parent_1]:
                rep[parent_1] = parent_2
            else:
                rep[parent_1] = parent_2
                size[parent_2] += 1
        
        return False
        
        
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        representative = {i:i for i in range(1, len(edges) + 1)} # space O(n)
        size = [1 for i in range(len(edges) + 1)]
        graph = defaultdict(list) # space O(n)
        
#         for start,end in edges:
#             graph[start].append(end) # Time O(n)
    
        ans = []
        for v1, v2 in edges:
            ans = self.union(representative, v1, v2,size)
            
            if ans:
                return [v1, v2]
                