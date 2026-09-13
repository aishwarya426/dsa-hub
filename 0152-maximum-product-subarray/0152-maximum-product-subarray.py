class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod=nums[0]
        maxprod=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=minprod*nums[i]
            v3=maxprod*nums[i]
            maxprod=max(v1,max(v2,v3))
            minprod=min(v1,min(v2,v3))
            ans=max(ans,max(maxprod,minprod))
        return ans