class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prev_sum = skill[0] + skill[-1]
        res = skill[0] * skill[-1]
        
        l = 1
        r = len(skill) - 2
        
        while l < r:
            if prev_sum != skill[l] + skill[r]:
                return -1
            
            res += (skill[l] * skill[r])
            
            l += 1
            r -= 1
            
        
        return res