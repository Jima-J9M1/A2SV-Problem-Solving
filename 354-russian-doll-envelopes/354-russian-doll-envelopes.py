class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda env:(env[0], -env[1]))
        
        for env in envelopes:
            indx = self.binarySearch(env[1], dp)
            
            if indx == len(dp):
                dp.append(env[1])
            else:
                dp[indx] = env[1]

        return len(dp)
    
    
    def binarySearch(self,num,dp):
        left = 0
        right = (len(dp))

        while left < right:
            mid = left + ((right - left) // 2)

            if dp[mid] >= num:
                right = mid
            else:
                left = mid + 1

        return left