class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.max_val = len(times)
        self.person = persons
        self.time = times
        self.leads = []
        lead = -1
        count = defaultdict(int)
        
        
        for p in persons:
            count[p] += 1
            if count[p] >= count[lead]:
                lead = p
                
            self.leads.append(lead)
                   
    def q(self, t: int) -> int:
        left = 0
        right = self.max_val
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.time[mid] > t:
                right = mid
            else:
                left = mid + 1
                
        
        
            
        
        return self.leads[left - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)