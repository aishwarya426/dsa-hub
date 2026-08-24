class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        mainans=[]
        nums.sort()
        for i in range(len(nums)):
            ans=[]
            l=i+1
            r=len(nums)-1
            req= -nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                if nums[l]+nums[r]==req:
                    mainans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l]+nums[r]>req:
                    r-=1
                else:
                    l+=1
        return mainans

            


        