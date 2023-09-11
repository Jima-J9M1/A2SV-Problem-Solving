class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        _dict = defaultdict(list)
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in _dict or len(_dict[groupSizes[i]]) < groupSizes[i]:
                _dict[groupSizes[i]].append(i)
            else:
                result.append(_dict[groupSizes[i]])
                _dict[groupSizes[i]] = [i]
         
        for key in _dict:
            result.append(_dict[key])
            
        return result