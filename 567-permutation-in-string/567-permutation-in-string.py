class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ptr = len(s1)
        _dict1 = Counter(s1)
        
        for i in range(len(s2) - ptr +1):
            
            _dict2 = Counter(s2[i:i + ptr])
            if _dict1 == _dict2:
                
                return True
            
        return False

#         l,r = 0,len(s2) - 1
#         _dict = Counter(s1)
#         res = []
        
#         if len(s1) == 1:
#             if s1[-1] in s2:
#                 return True
#             else:
#                 return False
            
#         while l < r:
            
#             if _dict[s2[l]] and _dict[s2[r]] and ((r - l + 1) == len(s1)):

#                 while l < r:
                    
#                     if not _dict[s2[l]] or not _dict[s2[r]]:
#                         return False
                    
#                     res.append(s2[l])
#                     res.append(s2[r])
                    
                    
#                     l += 1
#                     r -= 1
#                 continue
            
            
#             elif _dict[s2[l]] and _dict[s2[r]] and ((r - l + 1)) > len(s1):
#                 _dict[s2[l]] += 1
                
#                 while l < r and not _dict[s2[l]] or (( r - l + 1 ) != len(s1)):
#                     if not _dict[s2[l]] -= 1:
#                     _dict[s2[l]] -= 1
#                     l += 1
                    
#                 continue
                
                    
#             if l < r:
                
#                 if _dict[s2[l]]:
#                     _dict[s2[l]] -= 1
#                     r -= 1
#                     continue

#                 if _dict[s2[r]]:
#                     _dict[s2[r]] -= 1
#                     l += 1
#                     continue
                
#                 l += 1
#                 r -= 1
#         st = sorted(list(s1))
#         res.sort()
        
#         if st == res:
#             return True
        
#         return False
        