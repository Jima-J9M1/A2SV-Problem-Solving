class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(lambda: -1)
        right = 0
        stack  = []
        
        while right < len(nums2):
            
            while stack and stack[-1] < nums2[right]:
                dic[stack[-1]] = nums2[right]
                stack.pop()
                
            stack.append(nums2[right])
            right += 1
            
        return [dic[num] for num in nums1] 
                
                          