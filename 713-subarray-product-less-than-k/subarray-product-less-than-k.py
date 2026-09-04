class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        left = 0
        ans = 0
        
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        
        return ans