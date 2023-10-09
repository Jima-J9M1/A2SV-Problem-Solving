class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [0] * len(gas)
        
        for indx, (cur_gas, cur_cost) in enumerate(zip(gas, cost)):
            diff[indx] = cur_gas - cur_cost
            
        Neg = 0
        pos = 0
        max_indx = -1
        
        if diff[0] < 0:
            Neg = diff[0]
            
        else:
            pos = diff[0]
            max_indx = 0
        
        flag = False
        for i in range(1, len(gas)):
            
            if diff[i] > 0 and pos == 0:
                max_indx = i
                pos += diff[i]
            elif diff[i] > 0 and pos > 0:
                pos += diff[i]
                
            elif diff[i] < 0 and pos > 0:
                pos = pos + diff[i]
                if pos < 0:
                    Neg += pos
                    max_indx = -1
                    pos = 0
            else:
                Neg += diff[i]
                
                
        
                       
        return max_indx if Neg + pos >= 0 else -1
        