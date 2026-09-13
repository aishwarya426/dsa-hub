class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p)>len(s):
            return []
        ans=[]
        f=[0]*26
        for i in range(len(p)):
            f[ord(p[i])-ord('a')]+=1


        left=0
        right=len(p)-1
        freq=[0]*26
        for i in range(len(p)):
            freq[ord(s[i])-ord('a')]+=1
        


        while right+1<len(s):
            if tuple(freq)==tuple(f):
                ans.append(left)
            freq[ord(s[left])-ord('a')]-=1
            freq[ord(s[right+1])-ord('a')]+=1
            left+=1
            right+=1
        
        l=len(s)-len(p)
        fr=[0]*26
        for i in range(len(s)-len(p),len(s)):
            fr[ord(s[i])-ord('a')]+=1

        if tuple(fr)==tuple(f):
            ans.append(l)

        return ans

        



        return ans


