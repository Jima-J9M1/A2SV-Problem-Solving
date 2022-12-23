class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        #hashmap letter from a - i to 1 - 9 and from j - z to 10# - 26#
        start = 96
        hash_letter = {}
        for index in range(1,27):
            if index <= 9:
                hash_letter[str(index)] = chr(start + index)
            else:
                val_key = str(index) + "#"
                hash_letter[val_key] = chr(start + index)
                
                
        #decrypt the string 
        left = 0
        right = 0
        k = 3
        ans = ""
        index = 0
        length = len(s)
        #iterate to find the string in the hash map
        while index < length and right < length:
            
            if (right - left + 1) == k:
                if s[right] == "#":
                    ans += hash_letter[s[left: right + 1]]
                    left = right + 1
                    right = left
                else:
                    ans += hash_letter[s[left]]
                    left += 1
            # elif right == length - 1:
            #     for val in range(right - left + 1):
            #         ans += hash_letter[s[left]]
            #         left += 1
                    
            index += 1
            right += 1
            
            
        while left < length:
            ans += hash_letter[ s[left]]
            left += 1
        return ans
        