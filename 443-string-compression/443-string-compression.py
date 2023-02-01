class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 1
        
        
        while right < len(chars):
            
            if chars[left] != chars[right]:
                length = right - left
                
                if length > 1:
                    l = 0
                    length = str(length)

                    while l < len(length):
                        chars[left + 1] = length[l]
                        l += 1
                        left += 1
                
                left = right
                right += 1
                continue
                
            chars[right] = " "
            right += 1
        
        if chars[right - 1] == " ":
            length = right - left
            if length > 1:
                l = 0
                length = str(length)
                
                while l < len(length):
                    chars[left + 1] = length[l]
                    l += 1
                    left += 1
        ptr = 0
        while ptr < len(chars):
            if chars[ptr] == " ":
                chars.pop(ptr)
                continue
            
            ptr += 1
            