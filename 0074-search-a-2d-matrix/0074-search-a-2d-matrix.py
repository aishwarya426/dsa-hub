class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        row=len(matrix)
        col=len(matrix[0])
        j=row*col-1
        while i<=j:
            mid=(i+j)//2
            r=mid//col
            c=mid%col
            if(matrix[r][c]==target):
                return True
            elif target>matrix[r][c]:
                i=mid+1
            else:
                j=mid-1
        return False

        