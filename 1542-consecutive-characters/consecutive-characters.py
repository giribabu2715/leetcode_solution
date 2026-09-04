class Solution:
    def maxPower(self, s: str) -> int:
        max_len = curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
                max_len = max(max_len, curr)
            else:
                curr = 1
        return max_len