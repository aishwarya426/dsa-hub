class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        while i<=j:
            hours=0
            mid= (i+j)//2
            for k in piles:
                hours+= (k+mid-1)//mid 
            if hours<=h:
                j=mid-1
            else:
                i=mid+1
        return i
        