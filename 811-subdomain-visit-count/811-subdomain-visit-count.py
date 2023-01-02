class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        length = len(cpdomains)
        
        for ele in cpdomains:
            val = list(ele.split())
            domains[val[1]] += int(val[0])
            
            for index,new_ele in enumerate(val[1]):
                if index < (len(val[1]) - 1) and new_ele == '.':
                    domains[str(val[1][index + 1:])] += int(val[0])
            
            stack = []
        for ind,key in enumerate(domains):
            val = str(domains[key]) + " " +str(key) 
            stack.append(val)
        
        return stack
            