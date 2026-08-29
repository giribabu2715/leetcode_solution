class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def ispossible(weights,days,cap):
            load=0
            D=1
            for i in weights:
                if load+i<=cap:
                    load+=i
                else:
                    D+=1
                    load=i
            return D<=days
        l=max(weights)
        h=sum(weights)
        while l<h:
            mid=(l+h)//2
            N=ispossible(weights,days,mid)
            if N:
                h=mid
            else:
                l=mid+1
        
        return l

