class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestsum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=bestsum+nums[i]
            v2=nums[i]
            bestsum=max(v1,v2)
            ans=max(bestsum,ans)
        return ans
        