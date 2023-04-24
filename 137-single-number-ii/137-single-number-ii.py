class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         res = count.items()
#         ans = sorted(res, key=lambda x:x[1] )
        
#         return ans[0][0]
#         count = defaultdict(int)
#         shift = 0
#         min_val = 0
        
#         for num in nums:
#             min_val = min(min_val, num)
        
#         for num in nums:
#             if num < 0:
#                 sh = 1 << -(num) -1
#             else:
#                 sh = 1 << (num - min_val)
                
#             if count[num] == 1:
#                 shift |= sh
#                 count[num] += 1
#             else:
#                 shift ^= sh
#                 count[num] += 1
                
#         for num in nums:
#             if num < 0:
#                 sh = 1 << -(num) -1
#             else:
#                 sh = 1 << (num + (-min_val))
#             ans = shift & sh
#             if ans > 0:
#                 return num

        
        min_val = min(nums)
        
        if min_val >= 0:
            offset = 0
        else:
            offset = -min_val
        
        for indx in range(len(nums)):
            nums[indx] += (offset)
        
        res = 0
        for i in range(32):
            count = 0
            for ele in nums:
                shift = ele & (1 << i)
                if shift > 0:
                    count += 1
            
            if count % 3:
                res += 2**(i)
                
        return res - offset
            
        
#         for ele in nums:
#             if ele < 0:
#                 bit_rep += int(bin(-ele)[2:])
                
#             else:
#                 pos_val = (ele - min_val) + 1
#                 bit_rep += int(bin(pos_val)[2:])

#         print(bit_rep)
#         binary_rep = ""   
#         while bit_rep != 0:
            
#             rem = (bit_rep % 10) % 3

#             binary_rep = str(rem) + binary_rep
  
#             bit_rep //= 10
#             print(bit_rep, binary_rep)
            
#         single_numb = int(binary_rep, 2)
#         res = 0
        
#         if single_numb > (-min_val):
#             res = (single_numb + min_val) - 1
#         else:
#             res = -single_numb
            
#         return res