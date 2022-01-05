class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        zero=set(nums)
        if any(zero)==False:
            return "0"
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                    temp=str(nums[i])
                    nums[i]=str(nums[j])
                    nums[j]=str(temp)
        nums=list(map(str,nums))
        return "".join(nums)
