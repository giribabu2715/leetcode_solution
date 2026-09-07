class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=(10**9)+7
        end=[0]*26
        for ch in s:
            idx=ord(ch)-ord('a')
            total=sum(end)%mod
            end[idx]=(total+1)%mod
        return sum(end)%mod
