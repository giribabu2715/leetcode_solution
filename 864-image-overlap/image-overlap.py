from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        
        if not ones1 or not ones2:
            return 0
        
        cnt = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                cnt[(r2 - r1, c2 - c1)] += 1
        
        return max(cnt.values())