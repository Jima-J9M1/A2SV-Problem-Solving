class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference_bit = x ^ y
        # ans = 0
        
        return bin(difference_bit).count("1")
#         while difference_bit != 0:
            
#             if difference_bit & 1 != 0:
#                 ans += 1
                
#             difference_bit >>= 1
            
#         return ans