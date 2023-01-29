class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        res_value=0
        for i in nums:
            if count[i]>0:
                count[i]-=1
                res_value+=1
            else:
                count[k-i]+=1
        
        return res_value
    
      