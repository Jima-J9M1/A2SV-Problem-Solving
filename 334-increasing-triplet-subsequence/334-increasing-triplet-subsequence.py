class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        indx1, indx2,indx3 = -1,-1,-1
        
        flag = False
        for i in range(len(nums)):
            if indx1 == -1 or nums[i] <= nums[indx1]:
                indx1 = i

            elif indx2 == -1 or nums[i] <= nums[indx2]:
                indx2 = i
            else:
                flag = True
                
        if flag:
            return True
        
        return False

