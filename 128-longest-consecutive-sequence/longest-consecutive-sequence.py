class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_length = 0

        for num in num_set:

            # Check if num is the beginning
            if num - 1 not in num_set:

                current = num
                length = 1

                # Find consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length
        
