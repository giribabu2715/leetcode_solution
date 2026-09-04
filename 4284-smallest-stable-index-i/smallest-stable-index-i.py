class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suff_min[i] <= k:
                return i
        return -1
