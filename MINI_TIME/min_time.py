from typing import List
from collections import defaultdict,deque

from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        incoming = defaultdict(int)
        graph = defaultdict(list)
        
        for start,end in edges:
            graph[start].append(end)
            incoming[end] += 1
            
        task_queue = deque()
        minimum_time = defaultdict(int)
        level = 1
        for key in range(1, n + 1):
            # print(key)
            if incoming[key] == 0:
                # print("here")
                task_queue.append(key)
                
                
        while task_queue:
            len_level = len(task_queue)
            
            
            for _ in range(len_level):
                task = task_queue.popleft()
                minimum_time[task] = str(level)
                # print("here",minimum_time)
                
                for related_task in graph[task]:
                    incoming[related_task] -= 1
                    
                    if incoming[related_task] == 0:
                        task_queue.append(related_task)
                        
            level += 1
        ans = list(minimum_time.values())
        
        return " ".join(ans)
        
