class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        
        left = 0
        curr = 0
        ans = 0
        
        for right in range(n):
            curr += cost[right]
            while curr > maxCost and left <= right:
                curr -= cost[left]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
