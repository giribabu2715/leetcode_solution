class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        S = n * (n + 1) // 2
        k = n // m
        num2 = m * k * (k + 1) // 2
        return S - 2 * num2