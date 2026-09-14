class Solution:
    def abs(self,x: int)->int:
        if x<0:
            x*=-1
        return x

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum=nums[0]
        minsum=nums[0]
        ans=self.abs(nums[0])
        
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=minsum+nums[i]
            v3=maxsum+nums[i]
            minsum=min(v1,v2)
            maxsum=max(v1,v3)
            ans=max(ans,max(maxsum,self.abs(minsum)))
        return ans
        