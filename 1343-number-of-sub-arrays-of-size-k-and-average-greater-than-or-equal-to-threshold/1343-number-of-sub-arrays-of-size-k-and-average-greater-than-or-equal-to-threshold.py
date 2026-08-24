class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        firstsum=0
        for i in range(0,k):
            firstsum+=arr[i]
        if firstsum/k >= threshold:
            ans+=1
        i=0
        j=i+k-1
        while j+1<len(arr): 
            
            firstsum=firstsum -arr[i]+arr[j+1]
            if firstsum/k >=threshold:
                ans+=1
            i+=1
            j+=1

        return ans


        