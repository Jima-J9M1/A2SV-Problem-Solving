class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        number_of_dot = 0
        result = [[]]
        self.backTracking(0, "", number_of_dot, s, result)
        
        return result[0]
    def backTracking(self, indx, path, number_of_dot,s,result):
        if len(s) < indx:
            return
        
        
        if path.count(".") == 4 and  (len(s) + 4) == len(path):
            arr = path.split('.')
            
            
            arr.pop()
            flag = True
            for ele in arr:
                if len(ele) == 0 or int(ele) > 255:
                    flag = False
                elif len(ele) > 1 and ele[0] == "0":
                    flag = False
                           
            if flag:    
                result[0].append(path[:-1])
                
        for i in range(indx, len(s)):
            path += s[i]
            self.backTracking(i + 1, path + ".", number_of_dot + 1, s, result)
            