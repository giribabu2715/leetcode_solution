from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_odd = False
        has_even = False
        min_odd = float('inf')
        
        for x in nums1:
            if x % 2 == 1:
                has_odd = True
                if x < min_odd:
                    min_odd = x
            else:
                has_even = True
        
       
        if not has_odd or not has_even:
            return True
        
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
        
        return True