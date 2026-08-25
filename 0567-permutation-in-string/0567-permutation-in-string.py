class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        freq=[0]*26
        for ch in s1:
            freq[ord(ch)-ord('a')]+=1
        tuple(freq)

        f=[0]*26

        for i in range(len(s1)):
            f[ord(s2[i])-ord('a')]+=1
        if tuple(f)==tuple(freq):
            return True
        
        i=0
        k=i+(len(s1))-1
        while k+1<len(s2):
            f[ord(s2[i])-ord('a')]-=1
            f[ord(s2[k+1])-ord('a')]+=1
            if tuple(f)==tuple(freq):
                return True
            else:
                i+=1
                k+=1
        return False




        