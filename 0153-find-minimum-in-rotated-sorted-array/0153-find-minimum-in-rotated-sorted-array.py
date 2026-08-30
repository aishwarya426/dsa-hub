class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        mini=float('inf')
        minii=float('inf')
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>nums[j]:
                # min in right half
                i=mid+1
            else:
                j=mid-1
            mini=min(nums[mid],mini)
        return mini
