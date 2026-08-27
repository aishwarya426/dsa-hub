class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range (len(nums1)):
            maxnum=-1
            for j in range (len(nums2)):
                if nums1[i]==nums2[j]:
                    
                    if j+1==len(nums2):
                        maxsum=-1
                    else:
                        
                        for k in range(j+1,len(nums2)):
                            if nums2[k]>nums2[j] :
                                maxnum=nums2[k]
                                break
                            else :
                                maxnum=-1
            ans.append(maxnum)
        return ans
            