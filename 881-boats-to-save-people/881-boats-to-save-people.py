class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        
        
        while r > 0 and l < len(people) and l < r:
            
            if people[l] + people[r] > limit:
                res += 1
            else:
                res += 1
                l += 1
                
            r -= 1
            
            
        if l == r:
            res += 1
            
            
        return res