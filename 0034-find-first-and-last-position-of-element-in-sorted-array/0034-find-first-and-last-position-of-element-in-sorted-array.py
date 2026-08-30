class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        ans=-1
        ans2=-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                ans=mid
                j=mid-1
            elif target>nums[mid]:
                i=mid+1
            else:
                j=mid-1
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                ans2=mid
                i=mid+1
            elif target>nums[mid]:
                i=mid+1
            else:
                j=mid-1
        return ans,ans2