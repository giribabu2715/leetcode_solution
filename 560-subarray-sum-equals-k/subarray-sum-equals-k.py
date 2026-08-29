class Solution:
    def subarraySum(self, nums, k):
        freq = {0: 1}
        sum = 0
        count = 0

        for num in nums:
            sum += num

            if sum - k in freq:
                count += freq[sum - k]

            if sum not in freq:
                freq[sum] = 0

            freq[sum] += 1

        return count
        