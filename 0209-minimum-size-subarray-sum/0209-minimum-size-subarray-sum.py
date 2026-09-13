class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        count=0
        fc=float('inf')
        sum=0
        l=0
        r=0
        while r<n or sum>=target:
            if sum>=target:
                fc=min(fc,r-l)
                sum=sum-nums[l]
                l+=1
            else:
                sum+=nums[r]
                r+=1
        if fc==float('inf'):
            return 0
        else:
            return fc
            

        