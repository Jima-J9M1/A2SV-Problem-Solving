class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = count.items()
        ans = sorted(res, key=lambda x:x[1] )
        
        return ans[0][0]
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
        
#         print(shift)