class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count_first_ele_words = Counter(words[0])
        set_first_ele_words = set(words[0])
        ans = []
        
        for ele in set_first_ele_words:

            
            for indx in range(1,len(words)):
                count_ele = words[indx].count(ele)
                if count_ele != count_first_ele_words[ele]:
                    count_first_ele_words[ele] = min(count_first_ele_words[ele], count_ele)

            
            while count_first_ele_words[ele] != 0:
                ans.append(ele)
                count_first_ele_words[ele] -= 1
        
        return ans
        
        