class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Hash table: remainder → first index where this remainder appeared
        hash_table = {0: -1}
        
        prefix_sum = 0
        
        for i in range(len(nums)):
            # Calculate prefix sum
            prefix_sum += nums[i]
            
            # Get remainder when divided by k
            remainder = prefix_sum % k
            
            # If this remainder was seen before
            if remainder in hash_table:
                # Check if subarray length is at least 2
                if i - hash_table[remainder] >= 2:
                    return True
            else:
                # Store the first occurrence of this remainder
                hash_table[remainder] = i
                
        return False