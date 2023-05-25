class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if numOnes < k:
            add_one_zero = numOnes + numZeros
            if (add_one_zero) >= k:
                return numOnes
            if (k - add_one_zero) < numNegOnes:
                return numOnes - (k - add_one_zero)
            else:
                return numOnes - numNegOnes
                
        else:
            return k
            