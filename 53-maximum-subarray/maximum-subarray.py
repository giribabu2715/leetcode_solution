class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=float('-inf')
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum>m:
                m=sum
            if sum<0:
                sum=0
        return m
