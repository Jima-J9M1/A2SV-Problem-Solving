class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result = [0]
        visited = set()
        
        for indx in range(len(requests)):
            check_req = [0] * n
            path = []
            self.backTracking(indx, requests, visited, path, result, check_req)

                    
        return result[0]
    
    """
    @param: indx -> index 
    @param: requests -> requests
    @param: visited -> store valid request 
    @param: path -> store the valid element
    @param: result -> store the last result
    @param: check_req -> check if the element can move from one building to another 
    """
    def backTracking(self, indx, requests, visited, path, result, check_req):
        if len(requests) <= indx:
            return
        
        #check_req:  -1 if the person is moving to another buliding
        #check_req: 1 if the person is hired in the building
        
        indx_i = requests[indx][0]
        indx_j = requests[indx][1]
        check_req[indx_i] += -1
        check_req[indx_j] += 1
        
        visited.add(indx)
        path.append(indx)
        min_val = min(check_req)
        max_val = max(check_req)
        
        if max_val == 0 and min_val == 0:
            result[0] = max(len(path), result[0])
        
        for i in range(indx, len(requests)):
    
            if i not in visited:
                self.backTracking(i, requests, visited, path, result, check_req)
                
                
               
                stackTop = path.pop()
                indx_i = requests[stackTop][0]
                indx_j = requests[stackTop][1]
                check_req[indx_i] += 1
                check_req[indx_j] += -1
                visited.remove(stackTop)
                
        return 