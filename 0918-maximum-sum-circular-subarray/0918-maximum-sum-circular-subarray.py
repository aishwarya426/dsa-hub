class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmin=minsum=nums[0]
        currmax=maxsum=nums[0]
        ans=nums[0]
        totalsum=sum(nums)

        for i in range(1,len(nums)):
            
            currmin=min(currmin+nums[i],nums[i])
            minsum=min(minsum,currmin)
            currmax=max(currmax+nums[i],nums[i])
            maxsum=max(maxsum,currmax)
            ans=max(ans,max(maxsum,totalsum-minsum))
        if maxsum<0:
            return maxsum
        else:
            return ans

        