class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        task_to_do = []
        
        for indx , task in enumerate(tasks):
            task_to_do.append([*task,indx])
        
        task_to_do.sort(reverse=True, key=lambda task:task[0])
        heap= []
        time = 0
        
        while heap or task_to_do:
            if not heap:
                time = max(time, task_to_do[-1][0])
                
            while task_to_do and task_to_do[-1][0] <= time:
                
                _, process_time, indx = task_to_do.pop()
                heappush(heap, ( process_time, indx))
                
            process_time, indx = heappop(heap)
            time += process_time
            ans.append(indx)
            
        return ans