"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return 
        
        visited = set()
        copy_graph = [dict()]
        
        self.dfs(visited, node, copy_graph)
        
        
        return copy_graph[0][node]
        
    def dfs(self, visited, node, copy_graph):
        if node in visited:
            return
        
        visited.add(node)
        if node not in copy_graph[0]:
            copy_graph[0][node] = Node(node.val)
        
        for neighbor in node.neighbors:
            if neighbor not in copy_graph[0]:
                copy_graph[0][neighbor] = Node(neighbor.val)
                
            copy_graph[0][node].neighbors.append(copy_graph[0][neighbor])
            self.dfs(visited, neighbor, copy_graph)

                
        