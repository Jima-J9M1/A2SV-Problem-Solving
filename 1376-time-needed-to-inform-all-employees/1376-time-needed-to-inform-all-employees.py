class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict
        _dict = defaultdict(list)
        
        for idx, (val,price) in enumerate(zip(manager,informTime)):
            _dict[val].append((idx,price))
        
        def dfs(root):
            if _dict.get(root,None) is None:
                return 0
            
            else: 
                max_val = float("-inf")
                for val, price in _dict[root]:
                    max_val = max(max([dfs(val) + price]), max_val)
                    
            return max_val
        
        return dfs(-1)
            
        