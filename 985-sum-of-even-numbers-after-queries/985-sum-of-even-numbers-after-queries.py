class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        length = len(nums)
        total_even_sum = 0
        
        for ele in nums:
            
            if ele % 2 == 0:
                total_even_sum += ele
        

        for index in range(length):
            val,indx = queries[index]
            res = nums[indx] + val
            if res % 2 == 0:
                if nums[indx] % 2 == 0:
                    total_even_sum -= nums[indx]
                total_even_sum += res
            else:
                if nums[indx] % 2 == 0:
                    total_even_sum -= nums[indx]
            nums[indx] = res
            ans.append(total_even_sum)      
            
        return ans
        