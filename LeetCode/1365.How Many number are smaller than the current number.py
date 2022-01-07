class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[]
        for i in range(len(nums)):
            num=0
            n=nums[i]
            for j in range(len(nums)):
                if i!=j and n>nums[j]:
                    num=num+1
            count.append(num)

        return count
                 
