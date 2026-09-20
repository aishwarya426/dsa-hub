class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        alpha=26
        a=[0]*26

        for i in range(26):
            a[i]=alpha
            alpha-=1   
        print(a)

        for i in range(len(s)):
            rev=a[(ord(s[i])-ord('a'))]
            sum+=rev*(i+1)
        return sum
        
        