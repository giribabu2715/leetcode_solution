class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=1
        x=set(nums)
        for i in range(len(x)+1):
            if k in x:
                k+=1
            else:
                return k