class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        while l<=r:
            mid=(l+r)//2

            groups=1
            currentsum=0
            for num in nums:
                if currentsum+num<=mid:
                    currentsum+=num
                else :
                    groups+=1
                    currentsum=num
            
            if groups<=k:
                r=mid-1
            else:
                l=mid+1
        return l

            
                    
        