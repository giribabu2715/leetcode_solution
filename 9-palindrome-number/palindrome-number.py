class Solution:
    def isPalindrome(self, x: int) -> bool:
        p=x
        r=0
        while x>0:
            k=x%10
            r=(r*10)+k
            x=x//10
        if p==r:
            return True
        else:
            return False
        
        