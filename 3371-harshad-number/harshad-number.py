class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        p=x
        sum=0
        while x>0:
            k=x%10
            sum=sum+k
            x=x//10
        if p%sum==0:
            return sum
        else:
            return -1