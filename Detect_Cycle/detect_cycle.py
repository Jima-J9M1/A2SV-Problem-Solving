from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		graph = defaultdict(list)
		
		for indx in range(len(adj)):
		    for ele in adj[indx]:
		        graph[indx].append(ele)
		        
		colors = [0]*V
		
		for key in graph:
	        if self.hasCycle(key, graph, colors, -1):
	            return 1
	            
	   
	    return 0
	    
	def hasCycle(self, node, graph,colors, prev_node):
        if colors[node] == 2:
         return False
         
        if colors[node] == 1:
         return True
         
        colors[node] = 1
        
        for neighbor in graph[node]:
         
         if prev_node != neighbor:
             if self.hasCycle(neighbor, graph, colors, node):
                 return True
                 
                 
        colors[node] = 2
        return False
		        
		        
