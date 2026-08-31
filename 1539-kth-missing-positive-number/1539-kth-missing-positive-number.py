class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        j=len(arr)-1
        while i<=j:
            mid =(i+j)//2
            missing = arr[mid]-mid-1
            if missing<k:
                i=mid+1
            elif missing>=k:
                j=mid-1
            
            
        return i+k