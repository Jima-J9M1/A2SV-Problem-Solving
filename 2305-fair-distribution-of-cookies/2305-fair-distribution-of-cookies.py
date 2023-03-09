class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        # if len(cookies) == k:
        #     return max(cookies)
        
        cookies.sort(reverse = True)
        self.minm = float("+inf")
        self.bucket = [0] * k
        self.k = k
        print(cookies)
        self.backTracking(cookies,0, k)
        return self.minm
    
    def backTracking(self, cookies , idx, k):
        if idx >= len(cookies):
            self.minm = min(self.minm, max(self.bucket))
            return
        
        if self.minm < max(self.bucket):
            return 
        
        for i in range(k):
            self.bucket[i] += cookies[idx]
            self.backTracking(cookies,idx + 1, k)
            self.bucket[i] -= cookies[idx]
            
        return 