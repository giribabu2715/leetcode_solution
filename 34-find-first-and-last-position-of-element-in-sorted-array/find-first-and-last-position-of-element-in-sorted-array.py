class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            l=0
            r=len(nums)
            while l<r:
                mid=(l+r)//2
                if nums[mid]<x:
                    l=mid+1
                else:
                    r=mid
            return l
        l=search(target)
        r=search(target+1)-1
        if l<=r:
            return [l,r]
        return [-1,-1]