class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        m = n + k - 1
        r = 2 * k
        if r > m:
            return 0
        res = 1
        for i in range(r):
            res = res * (m - i) % MOD
            inv = pow(i + 1, MOD - 2, MOD)
            res = res * inv % MOD
        return res