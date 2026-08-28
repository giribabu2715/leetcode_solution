class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        l=0
        h=(r*c)-1
        while l<=h:
            mid=(l+h)//2
            row=mid//c
            col=mid%c
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<=target: 
                l=mid+1
            else:
                h=mid-1
        return False        
                
        