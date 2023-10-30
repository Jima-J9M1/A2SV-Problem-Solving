class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        min_val = logs[0][0]
        max_val = logs[-1][1]
                
        
        for log in logs:
            if max_val < log[1]:
                max_val = log[1]
                
        range_ = max_val - min_val
        prefix_sum = [0] * (range_ + 1)
        
                
        for log in logs:
            indx = log[0] - min_val
            indx2 = log[1] - min_val
            prefix_sum[indx] += 1
            prefix_sum[indx2] -= 1
            
        
        prefix_sum = list(accumulate(prefix_sum))
        
        ans = 0
        max_val = 0
        
        for i in range(len(prefix_sum)):
            if prefix_sum[i] > max_val:
                ans = i
                max_val = prefix_sum[i]
                
        
        return ans + min_val