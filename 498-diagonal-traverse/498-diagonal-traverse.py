class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        _dict = defaultdict(list)
        ans = []
        
        #hash element with their diagonal element         
        for i,val in enumerate(mat):
            
            for j in range(len(val)):
                
                if ( i+j ) % 2 == 0:
                    _dict[i + j].insert(0,val[j])
                    continue               
                    
                _dict[i + j].append(val[j])
                

        
        for key in _dict:
            ans += _dict[key][:]
        return ans
        