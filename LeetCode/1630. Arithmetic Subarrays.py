
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        bo=[]
        found='False'
        store=[]
        
        for i in range(len(l)):
            k=sorted(nums[l[i]:r[i]+1])
            store=[]
            for j in range(1,len(k)):
                if k[j]-k[j-1]==k[1]-k[0]:
                    found='True'
                else:
                    found='False'
                store.append(found)
            if 'False' in store:
                bo.append(False)
            else:
                bo.append(all(store))
