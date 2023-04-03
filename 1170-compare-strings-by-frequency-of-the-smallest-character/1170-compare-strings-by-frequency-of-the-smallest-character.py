class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words.sort(key=lambda x:x.count(min(x)))
        
        count_q = Counter(queries)
        count_w = Counter(words)
        
        ans = []
        
        for ele in queries:
            
            left = 0
            right = len(words)
            
            while left < right:
                mid = left + (right - left) // 2
            
                if words[mid].count(min(words[mid])) > ele.count(min(ele)):
                    right = mid 
                else:
                    left = mid + 1
            window = (len(words) - 1) - left + 1
            ans.append(window)

        return ans
        
        