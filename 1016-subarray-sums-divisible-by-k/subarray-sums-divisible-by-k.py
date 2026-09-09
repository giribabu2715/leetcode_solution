class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        count=0
        prefixsum=0
        for i in nums:
            prefixsum+=i
            rem=prefixsum%k
            if rem in prefix:
                count+=prefix[rem]
            if rem not in prefix:
                prefix[rem]=0
            prefix[rem]+=1
        return count
