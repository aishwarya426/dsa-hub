class Solution:

    # BRUTE FORCE


    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     ans=[]
    #     for i in range (len(nums1)):
    #         maxnum=-1
    #         for j in range (len(nums2)):
    #             if nums1[i]==nums2[j]:
    #                 for k in range(j+1,len(nums2)):
    #                     if nums2[k]>nums2[j] :
    #                         maxnum=nums2[k]
    #                         break
    #         ans.append(maxnum)
    #     return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mydict = {}
        stack = []
        ans = []

        for i in range(len(nums2) - 1):
            stack.append(nums2[i])

            while stack and nums2[i + 1] > stack[-1]:
                mydict[stack[-1]] = nums2[i + 1]
                stack.pop()

        while stack:
            mydict[stack[-1]] = -1
            stack.pop()

        mydict[nums2[-1]] = -1

        for i in range(len(nums1)):
            ans.append(mydict[nums1[i]])

        return ans



    


            