class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i=max(weights)
        j=0
        for k in weights:
            j+=k
    
        while i<=j:
            mid=(i+j)//2
            sum=0
            day=1
            for k in weights:
                if sum + k > mid:
                    day += 1
                    sum = k
                else:
                    sum += k

            if day<=days:
                j=mid-1
            else:
                i=mid+1
        return i
            

            


