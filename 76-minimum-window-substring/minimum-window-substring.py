from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)               # required frequency of each character
        missing = len(t)                # how many characters are still missing
        left = 0
        min_len = float("inf")
        start = 0
        
        for right, ch in enumerate(s):
            if need[ch] > 0:            # this character is still needed
                missing -= 1
            need[ch] -= 1               # consume one occurrence
            
            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left           
                left_ch = s[left]
                need[left_ch] += 1
                if need[left_ch] > 0:   
                    missing += 1
                left += 1
        
        return "" if min_len == float("inf") else s[start:start + min_len]