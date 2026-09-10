class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        if k>=length:
            k=k%length
        nums.reverse()
        nums[0:k]=nums[0:k][::-1]
        nums[k:length]=nums[k:length][::-1]
        