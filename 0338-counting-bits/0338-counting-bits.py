class Solution:
    def countBits(self, n: int) -> List[int]:
        # Given an integer value n 
        # Goal: is to return number of 1 in [0,1,....,n], length of n + 1
        # Approach: 
        #        1 -> Iterate througth n + 1
        #        2 -> Using bitmap count number of 1's in binary number i
        #        3 -> store number of 1's in the list
        #        4 -> return the list of number of 1's for each [0,1, ..., n] integers
        
        ones_count = []
        for indx in range(n + 1):
            num = indx
            count = 0
            
            while num != 0:
                if num & 1 == 1:
                    count += 1
                    
                num >>= 1
                                    
            ones_count.append(count)
            
        return ones_count