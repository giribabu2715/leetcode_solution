class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        count=0
        base=1000
        while base<=n:
            count+=n-base+1
            base*=1000
        return count