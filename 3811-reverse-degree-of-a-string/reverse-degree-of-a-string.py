class Solution:
    def reverseDegree(self, s):
        revDegree = 0
        n = len(s)
        for i in range(n):
            revDegree += (i + 1) * (26 - (ord(s[i]) - ord('a')))
        return revDegree